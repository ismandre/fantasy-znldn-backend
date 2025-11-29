from typing import cast, override

from adapters.types.sofascore_tournaments import UniqueTournamentResponse
from domain.errors.http_client import HTTPClientError
from domain.errors.tournament import TournamentNotFoundError
from domain.models.tournament import Tournament
from domain.ports.http_client import HttpClient
from domain.ports.tournament_repository import TournamentRepository


class SofascoreTournamentRepository(TournamentRepository):
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    @override
    async def get(self, tournament_id: int) -> Tournament:
        try:
            response = await self.http_client.get(f"https://api.sofascore.com/api/v1/unique-tournament/{tournament_id}")
            if "error" in response:
                if response["error"].get("code") == 404:
                    raise TournamentNotFoundError(f"Tournament with ID {tournament_id} not found")
            print(f"Response: {response}")
            response_data = cast(
                UniqueTournamentResponse,
                response
           )
            print(f"Tournament data: {response_data}")
        except HTTPClientError as e:
            if "404" in str(e):
                print(f"Tournament with ID {tournament_id} not found")
                raise TournamentNotFoundError
            print(f"HTTP error when fetching info for tournament {tournament_id}: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error when fetching info for tournament {tournament_id}: {e}")
            raise
        return self._map_response_to_domain_model(response_data)

    def _map_response_to_domain_model(self, response_data: UniqueTournamentResponse) -> Tournament:
        return Tournament(
            id=response_data["uniqueTournament"]["id"],
            name=response_data["uniqueTournament"]["name"],
            has_rounds=response_data["uniqueTournament"]["hasRounds"],
            start_date=response_data["uniqueTournament"]["startDateTimestamp"]
        )
