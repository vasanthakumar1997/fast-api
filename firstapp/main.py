from fastapi import FastAPI
from .api.router.router import v1
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI()

app.mount("/static", StaticFiles(directory=f"{os.getcwd}/firstapp/static"), name="static")
app.include_router(v1)