


def isValidDate(year, month, day):
    leapYear = False
    def givenDateNotValid():
        givenDate = (f"{year}/{month}/{day}")
        print(f"{givenDate} is not a valid date.")

    def isLeapYear(year):
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
        
        assert isLeapYear(1999) == False
        assert isLeapYear(2000) == True
        assert isLeapYear(2001) == False
        assert isLeapYear(2004) == True
        assert isLeapYear(2100) == False
        assert isLeapYear(2400) == True

    def monthChk(month):
        if not 1 <= month <= 12:
            print(f"The given number for month is not correct : {month}")
            givenDateNotValid()
            return False
        else:
            return True

    def dayChk(day):
        if str(month) in ["4","6","9","11"]:
            if not 1 <= day <= 30:
                print(f"The given number for day is not correct : {day}.\n"
                        "Days for September, April, June and November can\n"
                        "go up to 30.")
                givenDateNotValid()
                return False
            else:
                return True
        
        
        if int(month) == 2:
            maxDays = int()
            if isLeapYear(year):
                print(f"{year} is a leap year.")
                maxDays = int(29)
            elif not isLeapYear(year):
                maxDays = int(28)
        
            if not 1 <= day <= maxDays:
                print(f"The given number for day is not correct : {day}.\n"
                       "Days can go up to 28 in February (29 if a leap year).")
                givenDateNotValid()
                return False
            else:
                return True

        else:
            if not 1 <= day <= 31:
                print(f"The given number given for day is not correct : {day}.\n"
                       "Days can go up to 31 in January, March, May, July,     \n"
                       "October and December.")
                givenDateNotValid()
                return False
            else:
                return True
            
    
    
    if all([monthChk(month), dayChk(day)]):
        print(f"{year}/{month}/{day} is a valid date.")
        return True
    else:
        return False

isValidDate(2000, 2, 29) 


assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

 

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay


        
















