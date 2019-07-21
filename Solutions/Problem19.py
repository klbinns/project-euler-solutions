'''
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def is_sunday(date):
  return date[2] == 1

def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def get_days_of_month(month, year):
  if month in [4, 6, 9, 11]:
    return 30
  elif month in [1, 3, 5, 7, 8, 10, 12]:
    return 31
  else:
    return 29 if is_leap_year(year) else 28

def advance_day_of_week(date):
  month, year, day_of_week = date
  days_to_advance = get_days_of_month(month, year) % 7
  if day_of_week + days_to_advance <= 7:
    return day_of_week + days_to_advance
  else:
    return (day_of_week + days_to_advance) - 7

def advance_month_and_year(date):
  month, year, day_of_week = date
  if(month < 12):
    month += 1
  else:
    month = 1
    year += 1

  return (month, year)

def advance_date_one_month(date):
  day_of_week = advance_day_of_week(date)
  month, year = advance_month_and_year(date)
  
  return (month, year, day_of_week)

date = (1, 1901, 1)
sunday_count = 0

while date[1] < 2001:
  if is_sunday(date):
    sunday_count += 1

  date = advance_date_one_month(date)

print(sunday_count)
