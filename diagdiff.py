#https://www.hackerrank.com/challenges/diagonal-difference/problem
ma=[[11,2, 4],
[4, 5 ,6],
[10, 8, -12]]
def diagonalDifference(arr):
    leftdia=0
    rightdia=0
    absv=0
    for i in range(len(arr[0])):
        leftdia+=arr[i][i]
        rightdia+=arr[i][len(arr[0])-i-1]
    absv=abs(leftdia-rightdia)
    return absv
print(diagonalDifference(arr))
