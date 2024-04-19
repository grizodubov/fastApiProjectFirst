from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# from settings import DATABASE_URL
# from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# №1 Генерируем урл который позволяет алхимии понять где БД
# DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
from app.config import settings

# №2 Передаем урл при создании асинхронного движка
engine = create_async_engine(settings.DATABASE_URL)

# №3 Используем движек для создания сесий (транзакций) через сешнмейкер
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# №4 раньше в алхимии создавали переменную, теперь это класс от которого будем насловаться при создании моделей
# в нем будут акумулироваться метаданные о всех таблицах, чтобы можно было удобно работать с миграцией
class Base(DeclarativeBase):
    pass
