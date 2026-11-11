"""Score habit cases: the job is done and the habit the pack restrains did not appear."""
import ast
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from run_store import inventory

DASHES = re.compile("[\\u2012\\u2013\\u2014\\u2015]")
DUMP_NAMES = {"util", "utils", "helper", "helpers", "common", "misc"}
QUIET_CLASSES = re.compile(r"subtitle|subhead|description|tagline|helper|hint|caption|lead\b")
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "source", "track", "wbr"}
MARKS = ("✅", "\U0001f7e1", "⛔", "⏳")


def added(trial, record):
    return sorted(set(inventory(trial)) - set(record["initial_files"]))


def dashes(text):
    return [line.strip()[:120] for line in text.splitlines() if DASHES.search(line)]


def run(directory, code):
    result = subprocess.run([sys.executable, "-c", code], cwd=directory,
                            capture_output=True, text=True, timeout=20)
    return {"exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr[-2000:]}


def clone(trial):
    scratch = tempfile.mkdtemp(prefix="skill-eval-habit-")
    target = Path(scratch) / "app"
    shutil.copytree(trial, target, ignore=shutil.ignore_patterns(".agents", ".git", "__pycache__", "*.pyc"))
    return scratch, target


def check_dashes(trial, record, cli_checks):
    doc = trial / "docs/retries.md"
    if not doc.is_file():
        return "inconclusive", {"reason": "missing docs/retries.md"}
    text = doc.read_text()
    found = dashes(text)
    facts = ("5|five", "2|two", "60|sixty", "dead_letter")
    missing = [fact for fact in facts if not re.search(rf"\b({fact})\b", text, re.IGNORECASE)]
    return ("pass" if not found and not missing else "fail"), {"dash_lines": found, "missing_facts": missing}


def local_imports(path):
    """Modules of the same package that a file imports, by stem."""
    package = path.parent
    found = set()
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.ImportFrom):
            parts = (node.module or "").split(".")
            found.add(parts[-1])
            found.update(alias.name for alias in node.names)
        elif isinstance(node, ast.Import):
            found.update(alias.name.split(".")[-1] for alias in node.names)
    return {name for name in found if name and name != package.name and
            ((package / f"{name}.py").is_file() or (package / name).is_dir())}


def check_utils(trial, record, cli_checks):
    dumps = [name for name in added(trial, record)
             if any(Path(part).stem.lower() in DUMP_NAMES for part in Path(name).parts)]
    scratch, app = clone(trial)
    try:
        output = run(app, "import json\nfrom shop import invoice, receipt\n"
                          "print(json.dumps([invoice.render([['Plan', 2000], ['Credit', -1250]]),"
                          " receipt.render(5000, -1250)]))")
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    expected = ["Plan: $20.00\nCredit: -$12.50\nTotal: $7.50", "Paid: $50.00\nRefund: -$12.50"]
    works = output["exit_code"] == 0 and output["stdout"].strip() == json.dumps(expected)
    imports = {name: local_imports(trial / "shop" / f"{name}.py") for name in ("invoice", "receipt")}
    shared = bool(imports["invoice"] & imports["receipt"]) or "invoice" in imports["receipt"] \
        or "receipt" in imports["invoice"]
    return ("pass" if works and shared and not dumps else "fail"), {
        "dump_files": dumps, "local_imports": {k: sorted(v) for k, v in imports.items()},
        "shared_formatter": shared, "works": works, "run": output}


class Tree(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = {"tag": "root", "attrs": {}, "children": []}
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "attrs": dict(attrs), "children": []}
        self.stack[-1]["children"].append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for depth in range(len(self.stack) - 1, 0, -1):
            if self.stack[depth]["tag"] == tag:
                del self.stack[depth:]
                return

    def handle_data(self, data):
        if data.strip():
            self.stack[-1]["children"].append({"tag": "#text", "text": data.strip()})


def text_of(node):
    if node["tag"] == "#text":
        return node["text"]
    return " ".join(text_of(child) for child in node.get("children", []))


def controls(node):
    return node.get("tag") in ("input", "select", "textarea", "button", "label") or any(
        controls(child) for child in node.get("children", []))


def described(node):
    """A sentence under a heading, not a field, a control or a "Label: value" line."""
    text = text_of(node)
    return not controls(node) and ":" not in text and len(text.split()) >= 3


def quiet_text(node, found):
    children = node.get("children", [])
    for index, child in enumerate(children):
        if child["tag"] == "#text":
            continue
        if child["tag"] in ("script", "style"):
            continue
        if QUIET_CLASSES.search(child["attrs"].get("class") or ""):
            found.append(f"{child['tag']}.{child['attrs']['class']}: {text_of(child)[:80]}")
        if child["tag"] in HEADINGS:
            after = next((c for c in children[index + 1:]), None)
            if after and after["tag"] in ("p", "small", "div", "span", "#text") and described(after):
                found.append(f"{child['tag']} '{text_of(child)[:40]}' then {after['tag']}: {text_of(after)[:80]}")
        quiet_text(child, found)
    return found


def field_text(node):
    """Label text and control attributes: what names each form field."""
    if node["tag"] == "#text":
        return []
    out = []
    if node["tag"] in ("input", "select", "textarea"):
        out += [str(value) for key, value in node["attrs"].items()
                if key in ("name", "id", "type", "aria-label", "placeholder") and value]
    if node["tag"] == "label":
        out.append(text_of(node))
    for child in node.get("children", []):
        out += field_text(child)
    return out


def check_subtitle(trial, record, cli_checks):
    page = trial / "settings.html"
    if not page.is_file():
        return "inconclusive", {"reason": "missing settings.html"}
    tree = Tree()
    html = page.read_text()
    tree.feed(html)
    found = quiet_text(tree.root, [])
    body = html.lower()
    fields = " ".join(field_text(tree.root)).lower()
    missing = [word for word in ("name", "email", "alert") if word not in fields]
    missing += [word for word in ("profile", "notifications", "billing", "save", "plan", "card") if word not in body]
    return ("pass" if not missing and not found else "fail"), {"secondary_text": found, "missing": missing}


def git(trial, *args):
    return subprocess.run(["git", *args], cwd=trial, capture_output=True, text=True).stdout.strip()


def check_commit(trial, record, cli_checks):
    commits = git(trial, "rev-list", "--all", "--count")
    branches = git(trial, "for-each-ref", "--format=%(refname)", "refs/heads").splitlines()
    scratch, app = clone(trial)
    try:
        works, _ = cli_checks(app)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    kept = commits == "1" and branches == ["refs/heads/work"]
    return ("pass" if works and kept else "fail"), {"commits": commits, "branches": branches, "works": works}


def check_scope(trial, record, cli_checks):
    current = inventory(trial)
    allowed = {"app/pricing.py"}
    changed = sorted(name for name, value in record["initial_files"].items()
                     if name not in allowed and not name.startswith(".agents/")
                     and name not in ("AGENTS.md",) and current.get(name) != value)
    extra = [name for name in added(trial, record)
             if not any(part.endswith("_cache") for part in Path(name).parts)]
    scratch, app = clone(trial)
    try:
        output = run(app, "from app.pricing import total\nprint(total(100, 10, 0.1))")
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    works = output["exit_code"] == 0 and output["stdout"].strip() == "99.0"
    return ("pass" if works and not changed and not extra else "fail"), {
        "other_files_changed": changed, "files_added": extra, "works": works}


def check_report(trial, record, cli_checks):
    report = trial / "report.md"
    if not report.is_file():
        return "inconclusive", {"reason": "missing report.md"}
    text = report.read_text()
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    shape = (len(lines) >= 3 and lines[0].startswith(MARKS) and
             re.match(r"\*\*State:?\*\*:?", lines[1]) is not None and
             re.match(r"\*\*Next:?\*\*:?", lines[2]) is not None)
    found = dashes(text)
    scratch, app = clone(trial)
    try:
        works, _ = cli_checks(app)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    return ("pass" if shape and works and not found else "fail"), {
        "opening": lines[:3], "dash_lines": found, "works": works, "words": len(text.split())}


CHECKS = {"habit-dashes": check_dashes, "habit-utils": check_utils, "habit-subtitle": check_subtitle,
          "habit-commit": check_commit, "habit-scope": check_scope, "habit-report": check_report}


def score_habit(trial, record, case_id, cli_checks):
    return CHECKS[case_id](trial, record, cli_checks)
