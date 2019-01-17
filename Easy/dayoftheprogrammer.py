#https://www.hackerrank.com/challenges/day-of-the-programmer/problem
year=1600
import datetime

def dayOfProgrammer(year):
    dop=256
    month=9
    if  year==1918:
        day=dop-243+13
    elif year%4!=0 or (year%100==0 and year%400!=0) :
        day=dop-243
        #Not leap
    else:
        day=dop-243-1
        #Leap
    final= datetime.datetime(year, month, day)
    return str(final.strftime("%d.%m.%Y"))

print(dayOfProgrammer(year))
