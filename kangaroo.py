#https://www.hackerrank.com/challenges/kangaroo/problem
x1=43
v1=2
x2=70
v2=2
def kangaroo(x1, v1, x2, v2):
    if (x1>=x2 and v1>v2) or (x1>=x2 and v1>=v2):
        return "NO"
    elif (x2>=x1 and v2>v1) or (x2>x1 and v2>=v1):
        return "NO"
    elif abs(x1-x2)%abs(v1-v2)==0:
        return "YES"
    else:
        return "NO"

print(kangaroo(x1, v1, x2, v2))
