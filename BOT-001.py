from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()


@app.get("/hello/{name}")
async def read_item(name):
    response = "Hello" + name
    return {response}

def custom_openapi():
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


app.openapi = custom_openapi