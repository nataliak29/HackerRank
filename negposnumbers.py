
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
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

    posresult=posnum/len(arr)
    negresult=negnum/len(arr)
    zeresult=zeros/len(arr)
    print(posresult,negresult,zeresult)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
