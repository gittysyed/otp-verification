import datetime
from winsound import PlaySound
from playsound import playsound
import time

class Alarm:
    def __init__(self, datetime_obj):
        self.alarmtime = datetime_obj
        self.triggered = False

def set_alarm():
    alarms = []
    while True:
        date_input = input("Enter the Date (YYYY-MM-DD), or 'q' to quit:")
        if date_input == 'q':
            break
        time_input = input("Enter the time (HH:MM AM/PM):")
        alarm_datetime = datetime.datetime.strptime(date_input + ' ' + time_input, '%Y-%m-%d %I:%M %p')
        alarm = Alarm(alarm_datetime)
        alarms.append(alarm)
        print("Alarm Set for:", alarm_datetime)
    return alarms

def play_sound():
    sound_file = "C:\\Users\\ASUS\\Music\\Desktop\\success-fanfare-trumpets-6185.mp3"
    playsound(sound_file)

alarms = set_alarm()

while True:
    now = datetime.datetime.now()
    for alarm in alarms:
        if not alarm.triggered and now >= alarm.alarmtime:
            alarm.triggered = True
            print("Wake up!")
            play_sound()
    time.sleep(1)
