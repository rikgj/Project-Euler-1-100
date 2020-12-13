'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
import math

daysInMonth = [31,-1,31,30,31,30,31,31,30,31,30,31]
hits = 0
year = 1901
curDate = 6 # sunday 6. january 1901

while year <= 2000:
    print(year)
    for days in daysInMonth:
        print(curDate)
        if curDate == 1:
            hits+=1

        if days == -1:
             if year%4 == 0 and (year%400 == 0 or year%1000 != 0):
                 days = 29
             else:
                 days = 28

        curDate+= math.ceil((days-curDate)/7)*7 - days
        if curDate == 0:
            curDate = 7

    print('HITS' + str(hits))
    year+=1
print('TOTAL HITS: ' + str(hits))
