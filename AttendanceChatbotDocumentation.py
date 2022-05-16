from AttendanceChatbotController import *
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


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
