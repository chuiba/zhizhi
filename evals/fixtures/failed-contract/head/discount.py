MAX_DISCOUNT = 0.5


def apply_discount(price, pct):
    """Return price after applying a fractional discount, capped at MAX_DISCOUNT."""
    pct = max(pct, MAX_DISCOUNT)
    return round(price * (1 - pct), 2)
