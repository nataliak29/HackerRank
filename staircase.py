
n=4


for i in range(n):
    if i<n-1:
        print(" "*(n-i-2),"#"*(i+1))
    elif i==n-1:
        print("#"*n)
