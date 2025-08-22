__all__ = ["__version__"]
try:
    from importlib.resources import files
    _v = files(__package__).joinpath("../VERSION").read_text().strip()
except Exception:
    import os
    _v = os.getenv("APP_VERSION", "0.0.0")
__version__ = _v
