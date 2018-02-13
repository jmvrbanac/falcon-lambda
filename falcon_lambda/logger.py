import logging


def clear_root_handlers():
    root = logging.getLogger()

    for handler in root.handlers[:]:
        root.removeHandler(handler)


def setup_lambda_logger(level, format=None):
    """Clears root loggers and sets up a basic logging configuration."""
    clear_root_handlers()

    logging.basicConfig(
        level=level,
        format=format or '[%(levelname)s] [%(name)s] %(message)s'
    )
