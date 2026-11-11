import sys
def resetSeconds():
    hours = int(0)
    min = int(0)
    sec = int(0)

def reset_ask():
    answer = input("""

Enter something to continue or nothing to quit :
""")
    if answer == "":
        sys.exit()
    else:
        askSeconds()


def getHoursMinutesSeconds(totalSeconds):
    #TODO get Hours
    hours = int(0)
    min = int(0)
    sec = int(0)
    days = int(0)
    while totalSeconds >= 3600:
        totalSeconds -= 3600
        hours += int(1)

    #TODO get Min
    while totalSeconds >= 60:
        totalSeconds -= 60
        min += int(1)

    #TODO get sec
    sec = int(totalSeconds)

    #TODO convert result

    result = []
    if hours == 0 and min == 0 and sec == 0:
        convResult = "0s"
        return convResult
    while hours >= 24:
        hours -= 24
        days += 1

    if int(days) > int(0):
        days = str(days)
        days = (days + "d")
        result.append(days)
    if int(hours) > int(0):
        hours = str(hours)
        hours = (hours + "h")
        result.append(hours)
    if int(min) > int(0):
        min = str(min)
        min = (min + "m")
        result.append(min)
    if int(sec) > int(0):
        sec = str(sec)
        sec = (sec + "s")
        result.append(sec)
    convResult = str
    convResult = " ".join(result)
    print(convResult)
    reset_ask()

def askSeconds():
    try:
        time = int(input("""

Enter the number of seconds to process : 
"""))
        print(getHoursMinutesSeconds(time))
    except ValueError:
        print("You must enter a number.")
        askSeconds()
        return True

askSeconds()
resetSeconds()
reset_ask()



assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'