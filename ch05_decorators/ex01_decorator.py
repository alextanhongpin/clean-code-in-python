from functools import wraps
import logging

logger = logging.getLogger(__name__)


class ControlledException(Exception):
    """A generic exception on the program's domain."""


def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ControlledException as e:
                logger.info("retrying %s", operation.__qualname__)
                last_raised = e
            raise last_raised

    return wrapped
