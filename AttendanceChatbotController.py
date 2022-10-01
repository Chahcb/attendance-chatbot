from AttendanceChatbotDocumentation import *
from CreateAttendance import *
import json


@app.get("/hello/{name}")
def return_name(name):
    response = "Hello " + name
    return {response}


@app.post("/attendance")
def create_attendance(info_attendance: Message):
    name = info_attendance.message.sender.displayName
    result_attendance = createAttendance(info_attendance)
    result = {'text': '@' + name + ' : ' + result_attendance}
    return json.dumps(result, ensure_ascii=False)
