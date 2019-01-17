#https://www.hackerrank.com/challenges/staircase/problem
n=4


def staircase(n):

    for i in range(n):
        if i<n-1:
            print(" "*(n-i-2),"#"*(i+1))
        elif i==n-1:
            print("#"*n)


staircase(n)
