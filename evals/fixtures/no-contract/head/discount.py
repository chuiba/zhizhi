def apply_discount(price, pct):
    """Return price after applying a fractional discount."""
    return round(price * (1 - pct), 2)


def format_price(price):
    """Render a price for the receipt screen."""
    return f"${price:,.2f}"
