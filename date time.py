'''date and time'''

from datetime import datetime
now=datetime.now()
print(now)
currentday=now.day
currentmonth=now.month
currentyear=now.year
print("day", currentday , "month", currentmonth , "year", currentyear)