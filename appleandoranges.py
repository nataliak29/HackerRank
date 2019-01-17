#https://www.hackerrank.com/challenges/apple-and-orange/problem
s=7
t=11
a=5
b=15
apples=[-2,2,1]
oranges=[5,-6]
positionapples=[]
positionoranges=[]
counta=0
counto=0

for i in range(len(apples)):
    positionapples.append(apples[i]+a)
    if apples[i]+a<=t and apples[i]+a>=s:
        counta+=1
    else: continue
for j in range(len(oranges)):
    positionoranges.append(oranges[j]+b)
    if oranges[j]+b<=t and oranges[j]+b>=s:
        counto+=1
    else: continue


print(counta)
print(counto)
