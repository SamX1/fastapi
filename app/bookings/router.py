from fastapi import APIRouter, Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.users.models import User
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings(user: User = Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)




