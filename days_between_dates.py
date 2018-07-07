# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysInMonth(year, month):
    if ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
        return 30
    elif (month == 2):
        if (isLeapYear(year)):
            return 29
        else:
            return 28
    else:
        return 31

def nextDay(year, month, day):
    if (day < daysInMonth(year, month)):
        return year, month, day + 1
    else:
        if (month == 12):
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if (year1 < year2):
        return True
    elif (year1 == year2):
        if (month1 < month2):
            return True
        elif (month1 == month2):
            if (day1 < day2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def isLeapYear(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    day_count = 0
    while (dateIsBefore(year1, month1, day1, year2, month2, day2)):
        (year1, month1, day1) = nextDay(year1, month1, day1)
        day_count += 1
    return day_count

print(daysBetweenDates(2012,1,1,2012,2,28))     # OK!
print(daysBetweenDates(2012,1,1,2012,3,1))      # OK!
print(daysBetweenDates(2011,6,30,2012,6,30))    # off by +3
print(daysBetweenDates(2011,1,1,2012,8,8))      # off by +4
print(daysBetweenDates(1900,1,1,1999,12,31))    # off by +300
print(daysBetweenDates(2013,1,1, 2014,1,1))
print(daysBetweenDates(2012,1,1, 2013,1,1))

def test():
    # assert daysBetweenDates(2013,1,1, 2013,1,1) == 0
    # assert daysBetweenDates(2013,1,1, 2013,1,2) == 1
    # assert daysBetweenDates(2013,1,1, 2014,1,1) == 365
    # assert nextDay(2013,1,1) == (2013,1,2)
    # assert nextDay(2013,4,30) == (2013,5,1)
    # assert nextDay(2012,12,31) == (2013,1,1)
    # assert nextDay(2013,2,28) == (2013,3,1)
    # assert nextDay(2013,9,30) == (2013,10,1)
    # assert nextDay(2012,2,28) == (2012,2,29)
    # print("Assertions finished")

    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print("Test with data:", args, "failed")
            else:
                print("Test case passed!")
        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args)) 

test()