from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


# write the Create endpoint
@app.post("/", status_code=201)
def create_food(payload: Food):
    id = payload.id
    foods[payload.id] = payload
    return foods