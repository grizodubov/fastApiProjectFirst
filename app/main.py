from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.users.router import router as router_users  # задав псевдоним для удобства
from app.bookings.router import router as router_bookings  # задав псевдоним для удобства
from app.hotels.router import router as router_hotels

from app.pages.router import router as router_pages
from app.images.router import router as router_images


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)

app.include_router(router_pages)
app.include_router(router_images)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Origin", "Access-Control-Allow-Headers",
                   "Authorization"],
)
