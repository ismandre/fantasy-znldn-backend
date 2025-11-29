from abc import ABC, abstractmethod

from domain.models.tournament import Tournament


class TournamentRepository(ABC):
    @abstractmethod
    async def get(self, id: int) -> Tournament:
        """Get tournament by id."""
        pass