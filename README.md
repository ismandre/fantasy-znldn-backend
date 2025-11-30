
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
- [ ] POST /users
  - [X] define endpoint
  - [ ] define service layer
  - [ ] define serializers and schemas
  - [ ] define repository layer
  - [ ] connect endpoint to service layer
  - [ ] connect service layer to repository layer
  - [ ] implement actual repository layer
- [ ] POST /auth/login
  - [X] define endpoint
  - [ ] define service layer
  - [ ] define serializers and schemas
  - [ ] define repository layer
  - [ ] connect endpoint to service layer
  - [ ] connect service layer to repository layer
  - [ ] implement actual repository layer
- [ ] GET  /players
  - [X] define endpoint
  - [ ] define service layer
  - [ ] define serializers and schemas
  - [ ] define repository layer
  - [ ] connect endpoint to service layer
  - [ ] connect service layer to repository layer
  - [ ] implement actual repository layer
- [ ] GET  /players/{player_id}
  - [X] define endpoint
  - [ ] define service layer
  - [ ] define serializers and schemas
  - [ ] define repository layer
  - [ ] connect endpoint to service layer
  - [ ] connect service layer to repository layer
  - [ ] implement actual repository layer
- [ ] GET  /matches/upcoming
  - [X] define endpoint
  - [ ] define service layer
  - [ ] define serializers and schemas
  - [ ] define repository layer
  - [ ] connect endpoint to service layer
  - [ ] connect service layer to repository layer
  - [ ] implement actual repository layer
- [ ] GET  /matches/{match_id}
  - [X] define endpoint
  - [ ] define service layer
  - [ ] define serializers and schemas
  - [ ] define repository layer
  - [ ] connect endpoint to service layer
  - [ ] connect service layer to repository layer
  - [ ] implement actual repository layer
- [ ] GET  /users/{user_id}/squad
  - [X] define endpoint
  - [ ] define service layer
  - [ ] define serializers and schemas
  - [ ] define repository layer
  - [ ] connect endpoint to service layer
  - [ ] connect service layer to repository layer
  - [ ] implement actual repository layer
- [ ] POST /users/{user_id}/squad
  - [X] define endpoint
  - [ ] define service layer
  - [ ] define serializers and schemas
  - [ ] define repository layer
  - [ ] connect endpoint to service layer
  - [ ] connect service layer to repository layer
  - [ ] implement actual repository layer
- [ ] GET  /leaderboard
  - [X] define endpoint
  - [ ] define service layer
  - [ ] define serializers and schemas
  - [ ] define repository layer
  - [ ] connect endpoint to service layer
  - [ ] connect service layer to repository layer
  - [ ] implement actual repository layer
- [X] GET /tournament/{tournament_id}  
  - [X] define endpoint
  - [X] define service layer
  - [X] define serializers and schemas
  - [X] define repository layer
  - [X] connect endpoint to service layer
  - [X] connect service layer to repository layer
  - [X] implement actual repository layer
- [X] GET /tournament/{tournament_id}/seasons  
  - [X] define endpoint
  - [X] define service layer
  - [X] define serializers and schemas
  - [X] define repository layer
  - [X] connect endpoint to service layer
  - [X] connect service layer to repository layer
  - [X] implement actual repository layer



### SofScore API


1. [x] Retrieve tournament information from
- https://api.sofascore.com/api/v1/unique-tournament/16338

2. [X] Retrieve season information for that tournament from
- https://api.sofascore.com/api/v1/unique-tournament/16338/seasons

3. [X] Based on the latest season from step 2., retrieve rounds for that season
- https://api.sofascore.com/api/v1/unique-tournament/16338/season/81183/rounds

4. [X] For each round, retrieve matches for that round
- https://api.sofascore.com/api/v1/unique-tournament/16338/season/81183/events/round/10

5. For each match, retrieve incidents (goals, cards, ...) happened at that match

- https://api.sofascore.com/api/v1/event/14526964/incidents


[ ] Retrieve list of players for each team from

- https://www.sofascore.com/api/v1/team/368217/players