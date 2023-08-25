"""
Age practice
8/9 started
8/9 ended
"""

import datetime
date = datetime.date.today()
month = (date.strftime("%m"))
day = (date.strftime("%d"))
year = (date.strftime("%Y"))

print(int(year)-1)


birth_month = input("Enter your birth month (mm):")
birth_day = input("Enter your birth day(dd):")
birth_year = input("Enter your birth year(yyyy): ")
age = int(year) - int(birth_year)

if birth_month > month:
    print(f"You're {age - 1} years old")

else:
    print(f"You're {age} years old")