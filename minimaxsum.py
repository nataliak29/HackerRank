
arr=[5,5,5,5,5]
minsum=0
maxsum=0
print(arr.index(max(arr)))
if arr.index(max(arr))!=arr.index(min(arr)):
    for i in range(len(arr)):
        if arr.index(arr[i])!=arr.index(max(arr)):
            minsum+=arr[i]
        if arr.index(arr[i])!=arr.index(min(arr)):
            maxsum+=arr[i]
else:
    minsum=(len(arr)-1)*arr[0]
    maxsum=(len(arr)-1)*arr[0]
print(minsum,maxsum)
