#!/usr/bin/python2
# #####################################################################
# id_0019.py
#
# Przemyslaw Kaminski <cgenie@gmail.com>
# Time-stamp: <>
######################################################################

def days_in_month(m, year = 1901):
    # february
    if m == 2:
        if year % 400 == 0:
            return 29
        if year % 4 == 0 and year % 100 != 0:
            return 29
        else:
            return 28
    months = {1: 31,
              3: 31,
              4: 30,
              5: 31,
              6: 30,
              7: 31,
              8: 31,
              9: 30,
              10: 31,
              11: 30,
              12: 31}
    return months[m]

def day_of_week(year, month, day):
    # 1 Jan 1900 was Monday
    days = {0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday'
            }
    diffyears = year - 1900
    diffmonths = month - 0
    diffdays = day - 1
    d = 0
    for y in range(1900, year):
        #print "Year: " + str(y)
        if days_in_month(2, year = y) == 29:
            d += 366
        else:
            d += 365
    for m in range(1, month):
        #print "Month: " + str(m)
        d += days_in_month(m, year = year)
    for D in range(diffdays):
        #print "Day: " + str(D)
        d += 1
    return days[d % 7]

def ymd_increase_by_day(y, m, d):
    days = days_in_month(m, year = y)
    if d < days:
        d += 1
    else:
        m += 1
        d = 1
        if m > 12:
            y += 1
            m = 1
    return (y, m, d)

def ymd_slice((start_y, start_m, start_d), (end_y, end_m, end_d)):
    while True:
        yield((start_y, start_m, start_d))
        (start_y, start_m, start_d) = ymd_increase_by_day(start_y, start_m, start_d)
        if start_y == end_y:
            if start_m == end_m:
                if start_d == end_d:
                    break
        
if __name__ == '__main__':
    s = 0
    for y, m, d in ymd_slice((1901, 1, 1), (2001, 1, 1)):
        if d == 1:
            if day_of_week(y, m, d) == 'Sunday':
                s += 1
    print s
