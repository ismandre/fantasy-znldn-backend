from fastapi import APIRouter, status


router = APIRouter(prefix="/squads", tags=["squads"])


@router.get(
    path="/{user_id}/squad",
    name="Get user's squad",
    response_model=SquadSerializer,
    status_code=status.HTTP_200_OK
)
async def get_user_squad(user_id: int):
    return {}


@router.post(
    path="/{user_id}/squad",
    name="Update user's squad",
    response_model=SquadSerializer,
    status_code=status.HTTP_200_OK
)
async def update_user_squad(
        user_id: int,
        payload: CreateSquadRequest,
):
    return {}