DEFAULTS = {"currency": "USD", "tax_rate": 0.0}


def load_config(overrides=None):
    """Return the effective config: defaults overlaid with overrides."""
    cfg = dict(DEFAULTS)
    if overrides:
        cfg.update(overrides)
    return cfg
