from domain.models.tournament import Tournament, TournamentSeason
from domain.ports.tournament_repository import TournamentRepository


class TournamentService:
    def __init__(self, tournament_repository: TournamentRepository):
        self.tournament_repository = tournament_repository

    async def get_tournament(self, tournament_id: int) -> Tournament:
        return await self.tournament_repository.get(tournament_id)

    async def get_tournament_seasons(self, tournament_id: int) -> list[TournamentSeason]:
        return await self.tournament_repository.get_tournament_seasons(tournament_id)