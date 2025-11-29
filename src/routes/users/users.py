from typing import Annotated

from fastapi import APIRouter, status

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    path="",
    name="Create a new user",
    response_model=UserSerializer,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
        payload: CreateUserRequest,
        service: Annotated[UserService, depends(get_user_service)]
):
    return {}
