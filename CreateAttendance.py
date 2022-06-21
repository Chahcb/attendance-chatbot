from pydantic import BaseModel


class Name(BaseModel):
    displayName: str


class Room(BaseModel):
    displayName: str


class Attendance(BaseModel):
    text: str
    sender: Name


class Message(BaseModel):
    type: str
    message: Attendance
    space: Room

    class Config:
        schema_extra = {
            "example": {
                "type": "MESSAGE",
                "message": {"text": "@chatbot-attendance oxxox", "sender": {"displayName": "Jean Michel"}},
                "space": {"displayName": "some room"}
            }
        }


def cleanAttendance(text_attendance: Message):
    # Prend les 5 derniers caractères
    result = text_attendance.message.text[-5:]
    return result


def createAttendance(attendance: Message):
    presence: str = ""
    attendance_clean = cleanAttendance(attendance)
    for i in range(len(attendance_clean)):

        if attendance_clean[i] == 'o' or \
                attendance_clean[i] == 'O' or \
                attendance_clean[i] == '0' or \
                attendance_clean[i] == 'v' or \
                attendance_clean[i] == 'V':

            presence += " ✅ |"

        elif attendance_clean[i] == 'x' or \
                attendance_clean[i] == 'X' or \
                attendance_clean[i] == 'n' or \
                attendance_clean[i] == 'N':

            presence += " ❌ |"

        elif attendance_clean[i] == '?':
            presence += " ❓ |"

        else:
            presence += " ERROR |"
    presence = presence.rstrip(presence[-1])
    return presence
