from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

description = """
BOT pour simplifier l'écriture de la présence à la cantine dans le groupe google chat Présence 🚀

Retourne un affichage simple et coloré:

*  ✅ | ✅ | ✅ | ✅ | ✅ |
*  ❌ | ❌ | ❌ | ❌ | ❌ |
*  ❌ | ❌ | ✅ | ✅ | ❌ |
"""

tags_metadata = [
    {
        "name": "Nom",
    },
    {
        "name": "Présence à la cantine",
    },
]

app = FastAPI(openapi_tags=tags_metadata, docs_url="/documentation", redoc_url=None)


class Attendance(BaseModel):
    displayName: str
    attendance: str

    class Config:
        schema_extra = {
            "example": {
                "displayName": "Charline",
                "attendance": "oxxox",
            }
        }


@app.get("/hello/{name}", tags=["Nom"])
async def read_name(name):
    response = "Hello " + name
    return {response}


@app.post("/attendance", tags=["Présence à la cantine"])
async def create_attendance(info_attendance: Attendance):
    name = info_attendance.displayName
    presence = ""

    for i in range(len(info_attendance.attendance)):
        presence += info_attendance.attendance[i] + "|"
    presence = presence.rstrip(presence[-1])
    return {"text : ", name, " : ", presence}


def custom_documentation():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Attendance chatbot",
        version="1.0",
        description=description,
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_documentation
