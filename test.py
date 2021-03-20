import datetime

a = datetime.datetime.now()
print("jam =", a.hour)
print("menit =", a.minute)
print("detik =", a.second)
print("microsecond =", a.microsecond)

from datetime import time
a = time(5, 15, 5, 728172)
print("jam =", a.hour)
print("menit =", a.minute)
print("detik =", a.second)
print("microsecond =", a.microsecond)