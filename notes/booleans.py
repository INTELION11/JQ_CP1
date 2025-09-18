# JQ 1st Booleans Notes

import time 
import datetime as date



current_time = time.time()
readable_time = time.ctime(current_time)
new_current_time = date.datetime.now()
hour = new_current_time.strftime("%H")

# minutes = %M
# weekday = %A, #a
#day of month %D
# month = %B, %b
# number of month = %m
# year = %Y, %y
# seconds = %S
over = True

print(f"current time in seconds since january 1, 1970(epoch) {current_time}")
print(f"current time in  {readable_time}")
print(f"current time from date time  {new_current_time}")
print(f"the hour is {hour}")


print(f"the hour is saved as an intiger {isinstance(hour, int)}")
print(f"the hour is saved as an float {isinstance(hour, float)}")
print(f"the hour is saved as an string {isinstance(hour, str)}")
print(hour.isalpha())

print(f"has a value: {bool("Jacob")}")
print(f"has a value: {bool(False)}")
print(f"has a value: {bool(True)}")