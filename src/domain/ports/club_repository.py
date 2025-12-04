from abc import ABC, abstractmethod
from typing import List

from domain.models.club import ClubDetails


class ClubRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[ClubDetails]:
        """Get all clubs."""
        pass
