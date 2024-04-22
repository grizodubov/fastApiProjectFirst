from fastapi import APIRouter, Request

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix='/bookings',  # prefix for all endpoints in this router
    tags=['Bookings'],  # tag for grouping routes in swagger UI
)


@router.get("")
async def get_bookings(user):  # -> list[SBooking]:
    return await BookingDAO.find_all()
