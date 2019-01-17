#https://www.hackerrank.com/challenges/mini-max-sum/problem
arr=[5,5,5,5,5]

def miniMaxSum(arr):
    minsum=0
    maxsum=0

    if arr.index(max(arr))!=arr.index(min(arr)):
        for i in range(len(arr)):
            if arr.index(arr[i])!=arr.index(max(arr)):
                minsum+=arr[i]
            if arr.index(arr[i])!=arr.index(min(arr)):
                maxsum+=arr[i]
    else:
        minsum=(len(arr)-1)*arr[0]
        maxsum=(len(arr)-1)*arr[0]
    return minsum,maxsum

print(miniMaxSum(arr))
