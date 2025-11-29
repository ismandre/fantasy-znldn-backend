from abc import ABC, abstractmethod

from domain.models.tournament import Tournament, TournamentSeason


class TournamentRepository(ABC):
    @abstractmethod
    async def get(self, id: int) -> Tournament:
        """Get tournament by id."""
        pass

    @abstractmethod
    async def get_tournament_seasons(self, id: int) -> list[TournamentSeason]:
        """Get tournament seasons by tournament id."""
        pass