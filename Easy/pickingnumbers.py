#https://www.hackerrank.com/challenges/picking-numbers/problem
a=[4, 4,4,4,4]
import itertools

def pickingNumbers(a):
    filt_combin=[]
    combin=list(set(itertools.combinations(a, 2)))
    count=0
    lengths=[]
    for c in combin:
        if abs(c[0]-c[1])<=1 :
            filt_combin.append(c)
    for fc in filt_combin:
        count=0

        for ai in a:
            if ai==fc[0] or ai==fc[1]:
                count+=1
        lengths.append(count)


    return max(lengths)


print(pickingNumbers(a))
