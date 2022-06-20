from AttendanceChatbotDocumentation import *
from pydantic import BaseModel
from domain.CreateAttendance import *


class Attendance(BaseModel):
    attendance: str

    class Config:
        schema_extra = {
            "example": {
                "text": "✅ | ❓ | ✅ | ❌ | ❌",
            }
        }


@app.get("/hello/{name}", tags=["Nom"])
async def return_name(name):
    response = "Hello " + name
    return {response}


@app.post("/attendance", tags=["Présence à la cantine"])
def create_attendance(info_attendance: Attendance):
    return "'text : '" + {(attendance(info_attendance))}
