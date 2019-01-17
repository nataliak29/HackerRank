#https://www.hackerrank.com/challenges/simple-array-sum/problem
#Given an array of integers, find the sum of its elements.

ar=[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

def simpleArraySum(ar):
    total=0

    for i in range(len(ar)):
        total+=ar[i]
    return total

print(simpleArraySum(ar))
