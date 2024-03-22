from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


class HotelsSearchArgs:
    def __init__(self,
                 location: str = 'Алтай',
                 date_from: date = date(2020, 10, 5),
                 date_to: date = date(2020, 11, 5),
                 has_spa: Optional[bool] = None,
                 starts: Optional[int] = Query(None, ge=1, le=5)):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.starts = starts


@app.get("/hotels")
def get_hotels(search_arg: HotelsSearchArgs = Depends()) -> list[SHotel]:
    hotels = [
        {'address': "ул. Гагарина, 1, Алтай",
         'name': 'Super hotel',
         'stars': 5,
         }
    ]

    return hotels

