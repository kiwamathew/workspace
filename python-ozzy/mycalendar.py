# A calendar app
import calendar
year = int(input("Please enter a year of your choice: "))
month = int(input("Please enter a month of your choice: "))

m = calendar.month(year, month)
print(m)

