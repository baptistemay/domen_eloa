def ordinalSuffix(x):
    if x % 100 in (11,12,13):
        print(str(x) + "th")
    elif x % 10 == 1:
        print(str(x) + "st")
    elif x % 10 == 2:
        print(str(x) + "nd")
    elif x % 10 == 3:
        print(str(x) + "rd")
    else:
        print(str(x) + "th")
        
ordinalSuffix(0)
ordinalSuffix(1)
ordinalSuffix(2)
ordinalSuffix(3)
ordinalSuffix(4)
ordinalSuffix(10)
ordinalSuffix(11)
ordinalSuffix(12)
ordinalSuffix(13)
ordinalSuffix(14)
ordinalSuffix(101)

"""
assert ordinalSuffix(0) == '0th'

assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'
"""