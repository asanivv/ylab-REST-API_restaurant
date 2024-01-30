from fastapi import FastAPI

from .menu import models
from .menu.database import engine
from .menu.routers import menu_router

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(
    menu_router,
    prefix='/api/v1/menus'
)



