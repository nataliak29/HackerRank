#https://www.hackerrank.com/challenges/plus-minus/problem
arr =[-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    negnum=0
    posnum=0
    zeros=0
    for i in range(len(arr)):
        if arr[i]<0:
            negnum+=1
        elif arr[i]>0:
            posnum+=1
        else:
            zeros+=1
    posresult=posnum/n
    negresult=negnum/n
    zeresult=zeros/n
    return round(posresult,6)
    return round(negresult,6)
    return round(zeresult,6)

print(plusMinus(arr))
