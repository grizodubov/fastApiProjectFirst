from sqlalchemy import Column, Integer, String
from app.database import Base

# задаем модель которую потом перенесем в БД
class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)