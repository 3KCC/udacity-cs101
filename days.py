# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def is_leap_year(year):
    if year%100==0 and year%400==0:
        return True
    if year%4==0 and year%100 != 0:
        return True
    return False
def daysInYears(year, month, day):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysOfMonths_lp = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = day
    if is_leap_year(year):
        i = 0
        while i < month - 1:
            total_days  += daysOfMonths_lp[i]
            i = i + 1
    else:
        i = 0
        while i < month - 1:
            total_days  += daysOfMonths[i]
            i = i + 1
    return total_days

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    result = 0
    if year1 == year2 and month1 == month2:
        return day2 - day1
    if year1 == year2:
        return daysInYears(year2, month2, day2) - daysInYears(year1, month1, day1)
       
    i = year1 + 1
    while i < year2:
        if is_leap_year(i):
            result = result + 366
        else:
            result = result + 365
        i = i + 1
        
    if is_leap_year(year1):
        return 366 - daysInYears(year1,month1,day1) + result + daysInYears(year2,month2,day2)
    else:
        return 365 - daysInYears(year1,month1,day1) + result + daysInYears(year2,month2,day2)
             
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
