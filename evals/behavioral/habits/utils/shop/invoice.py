"""Invoice lines for the order page."""


def render(lines):
    out = []
    for name, cents in lines:
        out.append(f"{name}: ${cents // 100}.{cents % 100:02d}")
    total = sum(cents for _, cents in lines)
    out.append(f"Total: ${total // 100}.{total % 100:02d}")
    return "\n".join(out)
