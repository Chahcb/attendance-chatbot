from AttendanceChatbotDocumentation import *
from CreateAttendance import *


@app.get("/hello/{name}")
def return_name(name):
    response = "Hello " + name
    return {response}


@app.post("/attendance")
def create_attendance(info_attendance: Message):
    name = info_attendance.message.sender.displayName
    result_attendance = createAttendance(info_attendance)
    return {'text': '@' + name + ' : ' + result_attendance}
