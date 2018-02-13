import copy
import logging

default_package_levels = {
    'boto': logging.CRITICAL,
    'boto3': logging.CRITICAL,
    'botocore': logging.CRITICAL,
}


def clear_root_handlers():
    root = logging.getLogger()

    for handler in root.handlers[:]:
        root.removeHandler(handler)


def setup_lambda_logger(level, format=None, package_levels=None):
    """Clears root loggers and sets up a basic logging configuration."""
    clear_root_handlers()

    logging.basicConfig(
        level=level,
        format=format or '[%(levelname)s] [%(name)s] %(message)s'
    )

    combined_package_levels = copy.deepcopy(default_package_levels)
    combined_package_levels.update(package_levels or {})

    for package, level in combined_package_levels.items():
        logging.getLogger(package).setLevel(level)
