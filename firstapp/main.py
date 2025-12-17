from fastapi import FastAPI
from .api.router.router import v1
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.mount("/static", StaticFiles(directory="/mnt/c/Users/Vasanth/fastapi/firstapp/static"), name="static")
app.include_router(v1)