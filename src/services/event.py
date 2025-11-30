from domain.ports.event_repository import EventRepository


class EventService:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def get_incidents(self, event_id: int) -> list[EventIncidents]:
        return await self.event_repository.get_incidents(event_id)
