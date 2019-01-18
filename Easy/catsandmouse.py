#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
x=1
y=3
z=2

def catAndMouse(x, y, z):
    if abs(x-z)<abs(y-z):
        return "Cat A"
    elif abs(x-z)>abs(y-z):
        return "Cat B"
    else:
        return "Mouse C"


print(catAndMouse(x, y, z))
