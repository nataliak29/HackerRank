#https://www.hackerrank.com/challenges/sock-merchant/problem
ar=[10, 20, 20, 10, 10 ,30, 50, 10 ,20]
n=9

def sockMerchant(n, ar):
    sockpairs={}
    count=0
    for sock in ar:
        try:
            sockpairs[sock]+=1
        except:
            sockpairs[sock]=1
    socks=[(v) for k,v in sockpairs.items() ]
    for s in socks:
        if s%2==0:
            count+=s/2
        else: count+=(s-1)/2
    return int(count)



print(sockMerchant(n, ar))
