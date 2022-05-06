from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

app = FastAPI()


class Attendance(BaseModel):
    displayName: str
    attendance: str


@app.get("/hello/{name}")
async def read_name(name):
    response = "Hello " + name
    return {response}


@app.post("/attendance/")
async def create_attendance(attendance: Attendance):
    name = attendance.displayName
    presence = []

    for i in range(len(attendance.attendance)):
        presence.append(attendance.attendance[i])
        presence.append("|")
        affichage_presence = ""
        for word in presence:
            affichage_presence += str(word)
    print("text : ", name, " : ", affichage_presence)


def custom_documentation():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Attendance chatbot",
        version="1.0",
        description="Chatbot de présence à la cantine",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_documentation
