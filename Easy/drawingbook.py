#https://www.hackerrank.com/challenges/drawing-book/problem
n=6
p=5

def pageCount(n, p):
    count_start=0
    count_end=0
    curr_start=1
    curr_end=n
    while p>curr_start:
        count_start+=1
        curr_start+=2

    if n%2==0 and n-p==1:
        count_end=1
    else:
        while p<curr_end-1:
            count_end+=1
            curr_end-=2

    turns=[count_start,count_end]
    return min(turns)

print(pageCount(n, p))
