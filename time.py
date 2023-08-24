import time
timestamp=time.strftime("%H:%M:%S")
print("the time now is:",timestamp)
if timestamp>=("09:00:00") and timestamp<("12:00:00"):
    print("good morning sir")
elif timestamp>=("12:00:00") and timestamp<("18:00:00"):
    print("good afternoon sir")
else:
    print("good night sir")