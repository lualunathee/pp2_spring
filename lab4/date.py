#1 Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta
a = input("Input date in yy-mm-dd format: ")
try:
    b = datetime.strptime(a, "%Y-%m-%d")
    five_days_ago = b - timedelta(days=5)
    print(five_days_ago.strftime("%Y-%m-%d"))
except ValueError:
    print("Your input is wrong")
    
#2 Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta
a = input("Input date in yy-mm-dd format: ")
try:
    b = datetime.strptime(a, "%Y-%m-%d")
    yesterday = b - timedelta(days=1)
    tomorrow = b+timedelta(days=1)
    print("Yesterday: ", yesterday.strftime("%Y-%m-%d"))
    print("Today: ", b.strftime("%Y-%m-%d"))
    print("Tomorrow: ", tomorrow.strftime("%Y-%m-%d"))
except ValueError:
    print("Your input is wrong")
    
#3 Write a Python program to drop microseconds from datetime.
from datetime import*
c = input("Input date in yy-mm-dd format: ")
try:
    b = datetime.strptime(c, "%Y-%m-%d")
    d = b.replace(microsecond = 0)
    print(d)
except ValueError:
    print("Your input is wrong")
    
#4 Write a Python program to calculate two date difference in seconds
from datetime import *
e = input("Input first date in yy-mm-dd format: ")
f = input("Input second date in yy-mm-dd format: ")
try:
    a = datetime.strptime(e, "%Y-%m-%d")
    b = datetime.strptime(f, "%Y-%m-%d")
    difference = b - a
    difference_in_seconds= difference.total_seconds()
    print(difference_in_seconds)
except ValueError:
    print("Your input is wrong")