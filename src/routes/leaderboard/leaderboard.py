from fastapi import APIRouter, status


router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])



@router.get(
    path="/",
    name="Get leaderboard",
    response_model=LeaderboardSerializer,
    status_code=status.HTTP_200_OK
)
async def get_leaderboard():
    return {}