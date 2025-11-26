
# Fantasy League: 1. ŽNL Dubrovačko-neretvanska Backend

Backend service for the Fantasy League app for **1. ŽNL Dubrovačko-neretvanska**.
Provides API endpoints, database, admin panel, and data fetching from SofaScore.

## Tech Stack

* FastAPI
* SQLAlchemy
* PostgreSQL / SQLite
* Alembic
* sqladmin
* botasaurus

## Features

* Create users with a secret username
* Fetch matches, players, and events
* Manage user squads
* Calculate points and leaderboard
* Simple admin panel


## Running the Application

To run the application in development mode, use the command below:

```bash
python src/main.py
```

The API will be available at [http://localhost:9000](http://localhost:9000).

### API Docs

[http://localhost:9000/docs](http://localhost:9000/docs

## MVP API Proposal

- POST /users
- POST /auth/login
- GET /players
- GET /players/{player_id}
- GET /matches/upcoming
- GET /matches/{match_id}
- GET /users/{user_id}/squad
- POST /users/{user_id}/squad
- GET /leaderboard
