from fastapi import FastAPI
import uvicorn

from app.routes import xpto

api = FastAPI()

api.include_router(xpto.router)


def start():
    uvicorn.run("app:api", host="0.0.0.0", port=8000, reload=True)
