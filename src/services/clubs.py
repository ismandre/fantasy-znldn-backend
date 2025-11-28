from domain.ports.club_repository import ClubRepository


class ClubService:
    def __init__(self, club_repository: ClubRepository):
        self.club_repository = club_repository

    def get_all_clubs(self):
        return self.club_repository.get_all()
