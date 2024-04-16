from fastapi import APIRouter

from app.bookings.dao import BookingDAO

router = APIRouter(
    prefix='/bookings',  # prefix для всех эндпоинтов
    tags=['bookings'],  # тег для группировки эндпоинтов
)


@router.get("")
async def get_bookings():
    return await BookingDAO.find_all()
