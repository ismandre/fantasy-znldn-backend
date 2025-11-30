from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from domain.errors.event import EventNotFoundError

router = APIRouter(prefix="/events", tags=["events"])


@router.get(
    path="{event_id}/incidents",
    name="Get incidents",
    response_model=list[IncidentSerializer],
    status_code=status.HTTP_200_OK
)
async def get_incidents(
        event_id: int,
        service: Annotated[EventService, Depends(get_event_service)]
) -> list[IncidentSerializer]:
    try:
        incidents = service.get_event_incidents(event_id)
    except EventNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    return [IncidentSerializer.model_validate(incident) for incident in incidents]
