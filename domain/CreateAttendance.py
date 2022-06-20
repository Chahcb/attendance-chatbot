
def attendance(info_attendance):
    presence: str = ""
    for i in range(len(info_attendance.attendance)):

        if info_attendance.attendance[i] == 'o' or \
                info_attendance.attendance[i] == 'O' or \
                info_attendance.attendance[i] == '0' or \
                info_attendance.attendance[i] == 'v' or \
                info_attendance.attendance[i] == 'V':

            presence += " ✅ |"

        elif info_attendance.attendance[i] == 'x' or \
                info_attendance.attendance[i] == 'X' or \
                info_attendance.attendance[i] == 'n' or \
                info_attendance.attendance[i] == 'N':

            presence += " ❌ |"

        elif info_attendance.attendance[i] == '?':
            presence += " ❓ |"

        else:
            presence += " ERROR |"
    presence = presence.rstrip(presence[-1])
    return presence
