#https://www.hackerrank.com/challenges/counting-valleys/problem
n=8
s="UDDDUDUU"


def countingValleys(n, s):
    path=list(map(str, s))
    level_path=[]
    level=0
    valley=0

    for i in range(len(path)):
        if path[i]=='D':
            level-=1
            level_path.append(level)
        else:
            level+=1
            level_path.append(level)

    for j in range(len(level_path)):
        if level_path[j]<0 and level_path[j+1]==0:
            valley+=1


    return valley



print(countingValleys(n, s))
