import datetime
x = input("When is your next birthday? (Type in in the format of year, month, day):")
y = []
for d in range(0,10):
    y.append(x[d])
year = int(y[0] + y[1] + y[2] + y[3])
month = int(y[5] + y[6])
day = int(y[8] + y[9])
birthday = datetime.datetime(year, month, day)
today = datetime.datetime.today()
if today.year - year == 0:
    days = (birthday - today).days
    print(str(days) + " days until your birthday")
if today.year - year == -1:
    endofyear = datetime.datetime(today.year, 12, 31)
    untilend = (endofyear - today).days
    startofyear = datetime.datetime(today.year + 1, 1, 1)
    tilbday = (birthday - startofyear).days
    days = untilend + tilbday
    print(str(days + 2) + " days until your birthday")

