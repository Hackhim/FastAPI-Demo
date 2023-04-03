"""Module for a Fast API Demo"""
import random
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class CoingeckoCoin(BaseModel):
    """Model of a Coingecko Coin"""

    id: int
    symbol: str
    name: str
    country_origin: str
    sentiment_votes_up_percentage: Optional[float] = None
    sentiment_votes_down_percentage: Optional[float] = None
    market_cap_rank: Optional[int] = None
    coingecko_rank: int
    coingecko_score: float
    developer_score: float
    community_score: float
    liquidity_score: float
    public_interest_score: float


def generate_random_cg_coin(_id: int) -> CoingeckoCoin:
    """Generate a random Coingecko Coin"""
    return CoingeckoCoin(
        id=_id,
        symbol="TEST",
        name="Test Coin",
        country_origin="PirateBay",
        sentiment_votes_up_percentage=round(random.random(), 2),
        sentiment_votes_down_percentage=round(random.random(), 2),
        market_cap_rank=random.randrange(50, 1000),
        coingecko_rank=random.randrange(50, 1000),
        coingecko_score=round(random.uniform(0, 1000), 2),
        developer_score=round(random.uniform(0, 1000), 2),
        community_score=round(random.uniform(0, 1000), 2),
        liquidity_score=round(random.uniform(0, 1000), 2),
        public_interest_score=round(random.uniform(0, 1000), 2),
    )


app = FastAPI()


@app.get("/")
async def root():
    """Hello World !"""
    return {"message": "Hello World !"}


@app.get("/coingecko/coins")
async def list_coingecko_coins() -> list[CoingeckoCoin]:
    """List Coingecko Coins"""
    coins = []
    for i in range(15):
        coins.append(generate_random_cg_coin(i + 1337))
    return coins


@app.get("/coingecko/coins/{cg_id}")
async def retrieve_coingecko_coin(cg_id: int):
    """Retrieve a Coingecko Coin"""
    return generate_random_cg_coin(cg_id)
