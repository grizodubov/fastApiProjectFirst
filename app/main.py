from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.users.router import router as router_users  # задав псевдоним для удобства
from app.bookings.router import router as router_bookings  # задав псевдоним для удобства
from app.hotels.router import router as router_hotels
from app.pages.router import router as router_pages


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)

app.include_router(router_pages)
