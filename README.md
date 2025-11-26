
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

## Run (development)

```bash
uvicorn app.main:app --reload
```

## API Docs

[http://localhost:8000/docs](http://localhost:8000/docs)
