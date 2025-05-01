from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Bet(BaseModel):
    game: str
    team: str
    bookmaker: str
    odds: float
    ev: float

fake_bets = [
    {"game": "Lakers vs Celtics", "team": "Lakers", "bookmaker": "DraftKings", "odds": 2.1, "ev": 6.3},
    {"game": "Yankees vs Red Sox", "team": "Red Sox", "bookmaker": "FanDuel", "odds": 1.9, "ev": 4.8},
    {"game": "Packers vs Bears", "team": "Packers", "bookmaker": "BetMGM", "odds": 2.2, "ev": 7.5},
]

@app.get("/bets", response_model=List[Bet])
def get_bets():
    return fake_bets
