"""Render scored run roots as one Markdown comparison table."""
from cases import CASES
from scoring import score

EXPECTED = {case.id: case.expected for case in CASES}


def counts(results):
    return "/".join(str(sum(r["status"] == state for r in results))
                    for state in ("pass", "fail", "inconclusive"))


def cell(results):
    if not results:
        return "-"
    if len(results) > 1:
        return counts(results)
    result = results[0]
    if result["status"] != "fail":
        return result["status"]
    got = result["evidence"].get("artifact", {}).get("action")
    return "fail" if got is None else f"fail (got {got})"


def summarize(run_roots, labels):
    if len(labels) != len(run_roots):
        raise ValueError("number of labels must equal number of run roots")
    scored = [score(root)["results"] for root in run_roots]
    ids = list(dict.fromkeys(r["case"] for results in scored for r in results))
    rows = [["case", "expected", *labels]]
    rows += [[case_id, EXPECTED[case_id],
              *(cell([r for r in results if r["case"] == case_id]) for results in scored)]
             for case_id in ids]
    rows.append(["total p/f/i", "", *(counts(results) for results in scored)])
    lines = ["| " + " | ".join(row) + " |" for row in rows]
    lines.insert(1, "|" + " --- |" * len(rows[0]))
    return "\n".join(lines)
