from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from domain.errors.tournament import TournamentNotFoundError
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