#https://www.hackerrank.com/challenges/birthday-cake-candles/problem
ar_count=4
ar=[3,2,1,3]

def birthdayCakeCandles(ar):
    maxheight=max(ar)
    candles=0

    for i in range(ar_count):
        if ar[i]==maxheight:
            candles+=1

    return candles
