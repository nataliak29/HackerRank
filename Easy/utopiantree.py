#https://www.hackerrank.com/challenges/utopian-tree/problem
n=4

def utopianTree(n):
    h=1
    heights=[]
    for i in range(n+1):
        if i==0:
            h==1
        elif i%2==0:
            h+=1
        elif i%2!=0:
            h=h*2
    heights.append(h)
    return max(heights)

print( utopianTree(n))
