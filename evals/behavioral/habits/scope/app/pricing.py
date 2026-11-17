"""Checkout pricing."""


def total(subtotal, discount, tax_rate):
    """Return what the customer pays."""
    taxed = subtotal * (1 + tax_rate)
    return round(taxed - discount, 2)
