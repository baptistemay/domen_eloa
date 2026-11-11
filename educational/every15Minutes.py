minutesCount = 0
hoursCount = 0
minutesValue = ""
minutes = 0
hours = 0
am = True

for x in range(24):
    if hoursCount == 0:
        hours = "12"
    else:
        hours = str(hoursCount)
    if am == True:
        am_or_pm = "am"
    else:
        am_or_pm = "pm"
    for minutes in range(4):
        if minutesCount == 0:
            minutesValue = "00"
        else:
            minutesValue = int(minutesCount)
        print(hours + ":" + str(minutesValue) + " " + am_or_pm)
        minutesCount += 15
        minutesValue = int(minutesValue)
    hoursCount += 1
    if hoursCount > 11:
        hoursCount = 0
        am = False
    minutesCount = 0