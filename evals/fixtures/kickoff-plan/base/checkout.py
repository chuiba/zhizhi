from config import load_config
from discount import apply_discount


def total(price, pct, overrides=None):
    """Discounted price plus tax, per the effective config."""
    cfg = load_config(overrides)
    subtotal = apply_discount(price, pct)
    return round(subtotal * (1 + cfg["tax_rate"]), 2)
