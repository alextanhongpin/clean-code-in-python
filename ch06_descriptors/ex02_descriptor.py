import logging

logger = logging.getLogger(__name__)


class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        logger.info(f"Call: {self.__class__.__name__}.__get__({instance}, {owner})")
        return instance

class ClientClass:
    descriptor = DescriptorClass()
