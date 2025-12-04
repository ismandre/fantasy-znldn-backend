from abc import ABC, abstractmethod
from typing import Any


class HttpClient(ABC):
    @abstractmethod
    async def get(self, url: str) -> dict[str, Any]:
        pass
