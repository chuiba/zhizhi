def apply_discount(price, pct):
    """Return price after applying a fractional discount."""
    return round(price * (1 - pct), 2)
