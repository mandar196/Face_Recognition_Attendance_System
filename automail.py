import yagmail
import os

receiver = "kulkarnimandar96@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2020-09-30_19-13-43.csv"  # attach the file

# mail information
yag = yagmail.SMTP("kulkarnimandar96@gmail.com", "Mandar")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email sbody
    attachments=filename,  # file attached
)
