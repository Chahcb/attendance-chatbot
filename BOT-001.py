from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel


class Attendance(BaseModel):
    firstname: str
    attendance: str


app = FastAPI()


@app.get("/hello/{name}")
async def read_name(name):
    response = "Hello" + name
    return {response}


@app.post("/attendance/")
async def create_attendance(attendance: Attendance):
    return attendance


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Attendance chatbot",
        version="1.0",
        description="Chatbot de présence à la cantine",
        routes=app.routes,
    )

    # affiche le logo en haut à gauche
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
