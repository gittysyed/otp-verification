import datetime 
from playsound import playsound     
import time
class Alarm:
    def _init(self,datetime_obj):
        self.alarmtime = datetime_obj
        self.triggered = False
def set_alarm():
    alarms = []
while  True:
    date_input = input("Enter the Date (YYYY-MM-DD),or 'q' to quit:")
    if date_input == 'q':
        break
    time_input = input("Enter the time (HH:MM AM/PM):")
    alarm_datetime = datetime.datetime.strptime(date_input + ' '+ time_input, '%Y-%m-%d %I:%M %p')
    alarm = Alarm(alarm_datetime)
    print("Alarm Set for:",alarm_datetime)
while True:
    now = datetime.datetime.now()
    for alarm in alarms:
        if not alarm.triggered and  now >= alarm.datetime:
            alarm.triggered = True
            print("wake up!")
            play_sound()
    time.sleep(1) 
def play_sound():
    sound_file = ("C:\Users\ASUS\Music\Desktop\success-fanfare-trumpets-6185.mp3")  
    playsound(sound_file)
set_alarm()                 


