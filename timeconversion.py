#https://www.hackerrank.com/challenges/time-conversion/problem

s='11:05:45AM'


def timeConversion(s):
    timeofday=s[-2:]
    time=s[:-2]
    hour=time[:2]
    final=str()

    if timeofday=='PM' and int(hour)!=12 :
        final=str(int(hour)+12)+str(time[2:])
    elif timeofday=='AM' and int(hour)==12:
        final='00'+str(time[2:])
    else:
        final=str(time)
    return final


print(timeConversion(s))
