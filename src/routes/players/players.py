from fastapi import APIRouter, status

router = APIRouter(prefix="/players", tags=["players"])

@router.get(
    path="/",
    name="Get all players",
    response_model=list[PlayerSerializer],
    status_code=status.HTTP_200_OK
)
async def get_players():
    return []


@router.get(
    path="/{player_id}",
    name="Get player by ID",
    response_model=PlayerSerializer,
    status_code=status.HTTP_200_OK
)
async def get_player(player_id: int):
    return {}