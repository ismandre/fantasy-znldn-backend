from abc import ABC, abstractmethod

class EventRepository(ABC):
    @abstractmethod
    async def get_incidents(self, event_id: int) -> list[EventIncidents]:
        """Get incidents by event id."""
        pass
