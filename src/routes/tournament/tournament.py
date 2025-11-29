from fastapi import APIRouter, status



router = APIRouter(prefix="/tournament", tags=["tournament"])



@router.get(
    path="/",
    name="Get tournament info",
    response_model=TournamentSerializer,
    status_code=status.HTTP_200_OK
)
async def get_tournament_info():
    return {}