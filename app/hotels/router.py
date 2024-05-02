from datetime import date, datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Query
# from fastapi_cache.decorator import cache
from pydantic import TypeAdapter

from app.exceptions import CannotBookHotelForLongPeriod, DateFromCannotBeAfterDateTo
from app.hotels.dao import HotelsDAO
from app.hotels.rooms.router import router as router_room
from app.hotels.schemas import SHotel

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)
router.include_router(router_room)


@router.get("/{location}")
# @cache(expire=30)
async def get_hotels_by_location_and_time(
    location: str,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(
        ..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"
    ),
) -> list[SHotel]:
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongPeriod
    hotels = await HotelsDAO.find_all(location, date_from, date_to)
    hotels_parsed = TypeAdapter(list[SHotel]).validate_python(hotels)
    return hotels_parsed


@router.get("/id/{hotel_id}")
async def get_hotel_by_id(
    hotel_id: int,
) -> Optional[SHotel]:
    return await HotelsDAO.find_one_or_none(id=hotel_id)