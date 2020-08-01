"""Previous implementation uses three levels of nested operations. Cleaner approach is to use class parameters."""
from functools import wraps
import logging

logger = logging.getLogger(__name__)


class ControlledException(Exception):
    """A controlled exception"""


RETRIES_LIMIT = 3


class WithRetry:
    def __init__(self, retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
        self.retries_limit = retries_limit
        self.allowed_exceptions = allowed_exceptions or (ControlledException,)

    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in self.retries_limit:
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exceptions as e:
                    logger.info("retrying {operation} due to {e}")
                    last_raised = e

            return last_raised

        return wrapped
