from fastapi import APIRouter, status

router = APIRouter(prefix="/matches", tags=["matches"])

@router.get(
    path="/upcoming",
    name="Get all upcoming matches",
    response_model=[MatchSerializer],
    status_code=status.HTTP_200_OK
)
async def get_upcoming_matches():
    return []


@router.get(
    path="/{match_id}",
    name="Get match by ID",
    response_model=MatchSerializer,
    status_code=status.HTTP_200_OK
)
async def get_match(match_id: int):
    return {}