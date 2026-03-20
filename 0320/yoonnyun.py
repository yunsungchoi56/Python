year = int(input("Fnter a year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a laep year")
else:
    print(year, "is a common year.")