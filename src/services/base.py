from abc import ABC, abstractmethod

from src.models.base import BaseEvent


class MessageProducerABC(ABC):
    @abstractmethod
    async def publish(self, topic: str, message: str, key: str) -> None:
        ...


class MessageServiceABC(ABC):
    @abstractmethod
    async def send_message(
        self, topic: str, message: BaseEvent
    ) -> None:
        ...