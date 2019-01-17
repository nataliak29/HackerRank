
s=[2,2,1,3,2]
d=4
m=2

def birthday(s, d, m):
    splits=0
    for i in range(len(s)-m+1):
        if sum(s[i+ti] for ti in range(m)) ==d:
            splits+=1
    return splits

print(birthday(s, d, m))
