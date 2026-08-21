import logging

COMMANDS = ['init', 'dev', 'docker']

PROJECT = 'cc_tmpl_py'


class ColoredFormatter(logging.Formatter):
    """requirement: message excludes levelname."""
    COLORS = {  # noqa
        logging.DEBUG: "\033[1;36m",     # cyan
        logging.INFO: "\033[1;32m",      # green
        logging.WARNING: "\033[1;33m",   # yellow
        logging.ERROR: "\033[1;31m",     # red
        logging.CRITICAL: "\033[1;31m",  # bold red
    }
    RESET = "\033[0m"

    def format(self, record):
        color = self.COLORS.get(record.levelno, self.RESET)
        message = super().format(record)
        return f"{color}[{record.levelname}]{self.RESET} {message}"


_handler = logging.StreamHandler()
_handler.setFormatter(
    ColoredFormatter(
        "%(message)s"
    )
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(_handler)
