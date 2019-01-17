x1=43
v1=2
x2=70
v2=2
if (x1>=x2 and v1>v2) or (x1>=x2 and v1>=v2):
    print("NO")
elif (x2>=x1 and v2>v1) or (x2>x1 and v2>=v1):
    print("NO")
elif abs(x1-x2)%abs(v1-v2)==0:
    print("YES")
else: print("NO")
