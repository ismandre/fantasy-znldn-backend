from abc import ABC, abstractmethod

from domain.models.event import Event
from domain.models.round import TournamentRound
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

    @abstractmethod
    async def get_tournament_rounds(self, tournament_id, season_id) -> dict[str, TournamentRound | list[TournamentRound]]:
        """Get tournament rounds by tournament id and season id."""
        pass

    @abstractmethod
    async def get_tournament_round_events(self, tournament_id: int, season_id: int, round_number: int) -> list[Event]:
        """Get tournament round events by tournament id, season id and round number."""
        pass