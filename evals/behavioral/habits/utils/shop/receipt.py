"""Receipt text sent after checkout."""


def render(paid_cents, refund_cents):
    lines = [f"Paid: ${paid_cents // 100}.{paid_cents % 100:02d}"]
    if refund_cents:
        lines.append(f"Refund: ${refund_cents // 100}.{refund_cents % 100:02d}")
    return "\n".join(lines)
