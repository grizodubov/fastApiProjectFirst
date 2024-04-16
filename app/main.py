from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as router_bookings  # задав псевдоним для удобства

app = FastAPI()

app.include_router(router_bookings)

class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/hotels")
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5),
    
) -> list[SHotel]:
    hotels = [
        {
            "adress": "ул. Гагарина, 1, Алтай",
            "name": "Super Hotel",
            "stars": 5,
        },
    ]
    return hotels

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass