MAX_DISCOUNT = 0.4


def apply_discount(price, pct):
    """Return price after applying a fractional discount, capped at MAX_DISCOUNT."""
    pct = min(pct, MAX_DISCOUNT)
    return round(price * (1 - pct), 2)
