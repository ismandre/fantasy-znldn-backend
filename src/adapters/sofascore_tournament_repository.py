from typing import cast, override

from adapters.types.sofascore_tournaments import (
    UniqueTournamentResponse,
    UniqueTournamentSeasonEventsRoundResponse,
    UniqueTournamentSeasonRoundsResponse,
    UniqueTournamentSeasonsResponse,
)
from domain.errors.http_client import HTTPClientError
from domain.errors.tournament import TournamentNotFoundError
from domain.models.event import Event, EventStatus
from domain.models.round import TournamentRound
from domain.models.score import Score
from domain.models.team import Team
from domain.models.tournament import Tournament, TournamentSeason
from domain.ports.http_client import HttpClient
from domain.ports.tournament_repository import TournamentRepository


class SofascoreTournamentRepository(TournamentRepository):
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    @override
    async def get(self, tournament_id: int) -> Tournament:
        try:
            response = await self.http_client.get(
                f"https://api.sofascore.com/api/v1/unique-tournament/{tournament_id}"
            )
            if "error" in response:
                if response["error"].get("code") == 404:
                    raise TournamentNotFoundError(
                        f"Tournament with ID {tournament_id} not found"
                    )
            response_data = cast(UniqueTournamentResponse, response)
        except HTTPClientError as e:
            if "404" in str(e):
                print(f"Tournament with ID {tournament_id} not found")
                raise TournamentNotFoundError
            print(f"HTTP error when fetching info for tournament {tournament_id}: {e}")
            raise
        except Exception as e:
            print(
                f"Unexpected error when fetching info for tournament {tournament_id}: {e}"
            )
            raise
        return self._map_response_to_tournament_domain_model(response_data)

    @override
    async def get_tournament_seasons(
        self, tournament_id: int
    ) -> list[TournamentSeason]:
        try:
            response = await self.http_client.get(
                f"https://api.sofascore.com/api/v1/unique-tournament/{tournament_id}/seasons"
            )
            if "error" in response:
                if response["error"].get("code") == 404:
                    raise TournamentNotFoundError(
                        f"Tournament with ID {tournament_id} not found"
                    )
            response_data = cast(UniqueTournamentSeasonsResponse, response)
        except HTTPClientError as e:
            if "404" in str(e):
                print(f"Tournament with ID {tournament_id} not found")
                raise TournamentNotFoundError
            print(f"HTTP error when fetching info for tournament {tournament_id}: {e}")
            raise
        except Exception as e:
            print(
                f"Unexpected error when fetching info for tournament {tournament_id}: {e}"
            )
            raise
        return self._map_response_to_torunament_seasons_domain_model(response_data)

    @override
    async def get_tournament_rounds(
        self, tournament_id: int, season_id: int
    ) -> dict[str, TournamentRound | list[TournamentRound]]:
        try:
            response = await self.http_client.get(
                f"https://api.sofascore.com/api/v1/unique-tournament/{tournament_id}/season/{season_id}/rounds"
            )
            print(f"Response: {response}")
            if "error" in response:
                if response["error"].get("code") == 404:
                    raise TournamentNotFoundError(
                        f"Tournament with ID {tournament_id} not found"
                    )
            response_data = cast(UniqueTournamentSeasonRoundsResponse, response)
        except HTTPClientError as e:
            print(f"HTTP error when fetching info for tournament {tournament_id}: {e}")
            raise
        except Exception as e:
            print(
                f"Unexpected error when fetching info for tournament {tournament_id}: {e}"
            )
            raise
        return self._map_response_to_tournament_season_rounds_model(response_data)

    @override
    async def get_tournament_round_events(
        self, tournament_id: int, season_id: int, round_number: int
    ) -> list[Event]:
        try:
            response = await self.http_client.get(
                f"https://api.sofascore.com/api/v1/unique-tournament/{tournament_id}"
                f"/season/{season_id}/events/round/{round_number}"
            )
            if "error" in response:
                if response["error"].get("code") == 404:
                    raise TournamentNotFoundError(
                        f"Tournament with ID {tournament_id} not found"
                    )
            response_data = cast(UniqueTournamentSeasonEventsRoundResponse, response)
        except HTTPClientError as e:
            print(f"HTTP error when fetching info for tournament {tournament_id}: {e}")
            raise
        except Exception as e:
            print(
                f"Unexpected error when fetching info for tournament {tournament_id}: {e}"
            )
            raise
        return self._map_response_to_tournament_season_round_events_model(response_data)

    def _map_response_to_tournament_season_round_events_model(
        self, response_data: UniqueTournamentSeasonEventsRoundResponse
    ) -> list[Event]:
        return [
            Event(
                tournament=Tournament(
                    id=event["tournament"]["id"], name=event["tournament"]["name"]
                ),
                season=TournamentSeason(
                    id=event["season"]["id"],
                    name=event["season"]["name"],
                    year=event["season"]["year"],
                ),
                home_team=Team(
                    id=event["homeTeam"]["id"], name=event["homeTeam"]["name"]
                ),
                away_team=Team(
                    id=event["awayTeam"]["id"], name=event["awayTeam"]["name"]
                ),
                home_score=Score(
                    current=event["homeScore"]["current"],
                    display=event["homeScore"]["display"],
                    period1=event["homeScore"]["period1"],
                    period2=event["homeScore"]["period2"],
                    normaltime=event["homeScore"]["normaltime"],
                ),
                away_score=Score(
                    current=event["awayScore"]["current"],
                    display=event["awayScore"]["display"],
                    period1=event["awayScore"]["period1"],
                    period2=event["awayScore"]["period2"],
                    normaltime=event["awayScore"]["normaltime"],
                ),
                start_timestamp=event["startTimestamp"],
                status=EventStatus(
                    description=event["status"]["description"],
                    type=event["status"]["type"],
                ),
                round_info=TournamentRound(
                    round=event["roundInfo"]["round"],
                ),
            )
            for event in response_data["events"]
        ]

    def _map_response_to_tournament_season_rounds_model(
        self, response_data: UniqueTournamentSeasonRoundsResponse
    ) -> dict[str, TournamentRound | list[TournamentRound]]:
        return {
            "current_round": TournamentRound(
                round=response_data["currentRound"]["round"]
            ),
            "rounds": [
                TournamentRound(round=round["round"])
                for round in response_data["rounds"]
            ],
        }

    def _map_response_to_tournament_domain_model(
        self, response_data: UniqueTournamentResponse
    ) -> Tournament:
        return Tournament(
            id=response_data["uniqueTournament"]["id"],
            name=response_data["uniqueTournament"]["name"],
            has_rounds=response_data["uniqueTournament"]["hasRounds"],
            start_date=response_data["uniqueTournament"]["startDateTimestamp"],
        )

    def _map_response_to_torunament_seasons_domain_model(
        self, response_data: UniqueTournamentSeasonsResponse
    ) -> list[TournamentSeason]:
        return [
            TournamentSeason(id=season["id"], name=season["name"], year=season["year"])
            for season in response_data["seasons"]
        ]
