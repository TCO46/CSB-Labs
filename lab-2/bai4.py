import datetime


date1 = input("Date in MM/DD/YYYY format: ")
date2 = datetime.datetime.strptime(date1, "%m/%d/%Y").strftime("%d/%m/%y")

print(date2)