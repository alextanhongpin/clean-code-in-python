from functools import wraps
import logging

logger = logging.getLogger(__name__)

RETRIES_LIMIT = 3


class ControlledException(Exception):
    "random exception"


def with_retry(retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
    allowed_exceptions = allowed_exceptions or (ControlledException,)

    def retry(operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in retries_limit:
                try:
                    return operation(*args, **kwargs)
                except allowed_exceptions as e:
                    logger.info("retrying {operation} due to {e}")
                    last_raised = e
            raise last_raised

        return wrapped

    return retry


@with_retry()
def run_operation(task):
    task.run()


@with_retry(retries_limit=5)
def run_with_custom_retries_limit(task):
    task.run()


@with_retry(allowed_exceptions=(AttributeError,))
def run_with_custom_exceptions(task):
    task.run()


@with_retry(retries_limit=4, allowed_exceptions=(ZeroDivisionError, AttributeError))
def run_with_custom_parameters(task):
    task.run()
