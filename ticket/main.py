from fastapi import FastAPI
from .schemas.validata import *
from models.model import *
from .models.model import router


app = FastAPI(title="Online-Tickets")

app.include_router(router)

if __name__=():
    uni