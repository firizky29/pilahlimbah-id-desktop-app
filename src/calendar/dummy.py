"""
    try import calendar
"""
import calendar

year = int(input(""))
month = int(input(""))

calendar.setfirstweekday(calendar.SUNDAY)
cal = calendar.month(year,month)
print(cal)
