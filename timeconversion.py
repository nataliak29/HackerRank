s='11:05:45AM'
timeofday=s[-2:]
time=s[:-2]
hour=time[:2]

if timeofday=='PM' and int(hour)!=12 :
    print(str(int(hour)+12)+time[2:])
elif timeofday=='AM' and int(hour)==12:
    print('00'+time[2:])
else:
    print(time)
