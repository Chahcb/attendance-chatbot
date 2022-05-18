from AttendanceChatbotDocumentation import *
from pydantic import BaseModel


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
async def return_name(name):
    response = "Hello " + name
    return {response}


@app.post("/attendance", tags=["Présence à la cantine"])
def create_attendance(info_attendance: Attendance):
    name = info_attendance.displayName
    presence: str = ""

    for i in range(len(info_attendance.attendance)):

        if info_attendance.attendance[i] == 'o' or \
                info_attendance.attendance[i] == 'O' or \
                info_attendance.attendance[i] == '0' or \
                info_attendance.attendance[i] == 'v' or \
                info_attendance.attendance[i] == 'V':

            presence += "✅|"

        elif info_attendance.attendance[i] == 'x' or \
                info_attendance.attendance[i] == 'X' or \
                info_attendance.attendance[i] == 'n' or \
                info_attendance.attendance[i] == 'N':

            presence += "❌|"

        elif info_attendance.attendance[i] == '?':
            presence += "❓|"

        else:
            presence += " ERROR |"

    presence = presence.rstrip(presence[-1])
    return {name, presence}
