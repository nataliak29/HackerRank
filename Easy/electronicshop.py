#https://www.hackerrank.com/challenges/electronics-shop/problem
keyboards=[4]
drives=[5]
b=5

def getMoneySpent(keyboards, drives, b):
    try:
        result= b-min([b-(key+dri) for key in keyboards for dri in drives if b-(key+dri)>=0 ])
    except:
        result= -1

    return result

print(getMoneySpent(keyboards, drives, b))
