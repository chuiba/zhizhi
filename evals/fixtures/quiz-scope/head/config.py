DEFAULTS = {"currency": "USD", "tax_rate": 0.08}


def load_config(overrides=None):
    """Return the effective config: defaults overlaid with overrides."""
    cfg = dict(DEFAULTS)
    if overrides:
        cfg.update(overrides)
    if cfg["tax_rate"] < 0:
        raise ValueError("tax_rate must be >= 0")
    return cfg
