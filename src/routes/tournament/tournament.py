from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from domain.errors.round import RoundNotFoundError
from domain.errors.season import TournamentSeasonNotFoundError
from domain.errors.tournament import TournamentNotFoundError
from serializers.event import TournamentRoundEventSerializer
from serializers.round import TournamentRoundsSerializer, TournamentRoundSerializer
from serializers.season import SeasonSerializer
from serializers.tournament import TournamentSerializer
from services.deps import get_tournament_service
from services.tournament import TournamentService

router = APIRouter(prefix="/tournament", tags=["tournament"])



@router.get(
    path="/{tournament_id}",
    name="Get tournament info",
    response_model=TournamentSerializer,
    status_code=status.HTTP_200_OK
)
async def get_tournament_info(
        tournament_id: int,
        service: Annotated[TournamentService, Depends(get_tournament_service)]
) -> TournamentSerializer:
    try:
        tournament = await service.get_tournament(tournament_id)
    except TournamentNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    return TournamentSerializer.model_validate(tournament)


@router.get(
    path="/{tournament_id}/seasons",
    name="Get tournament seasons",
    response_model=list[SeasonSerializer],
    status_code=status.HTTP_200_OK
)
async def get_tournament_seasons(
        tournament_id: int,
        service: Annotated[TournamentService, Depends(get_tournament_service)]
) -> list[SeasonSerializer]:
    try:
        seasons = await service.get_tournament_seasons(tournament_id)
    except TournamentNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    return [SeasonSerializer.model_validate(season) for season in seasons]

@router.get(
    path="/{tournament_id}/seasons/{season_id}/rounds",
    name="Get tournament rounds for a given season",
    response_model=TournamentRoundsSerializer,
    status_code=status.HTTP_200_OK
)
async def get_tournament_rounds(
        tournament_id: int,
        season_id: int,
        service: Annotated[TournamentService, Depends(get_tournament_service)]
) -> TournamentRoundsSerializer:
    try:
        rounds = await service.get_tournament_rounds(tournament_id, season_id)
    except TournamentNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except TournamentSeasonNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    return TournamentRoundsSerializer(
        current_round=TournamentRoundSerializer.model_validate(rounds["current_round"]),
        rounds=[TournamentRoundSerializer.model_validate(round) for round in rounds["rounds"]]
    )



@router.get(
    path="/{tournament_id}/season/{season_id}/events/round/{round}",
    name="Get tournament events for a given round",
    response_model=list[TournamentRoundEventSerializer],
    status_code=status.HTTP_200_OK
)
async def get_events_for_round(
        tournament_id: int,
        season_id: int,
        round: int,
        service: Annotated[TournamentService, Depends(get_tournament_service)]
) -> list[TournamentRoundEventSerializer]:
    try:
        events = await service.get_tournament_round_events(tournament_id, season_id, round)
    except TournamentNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except TournamentSeasonNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    except RoundNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    return [TournamentRoundEventSerializer.model_validate(event) for event in events]

