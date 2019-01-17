ma=[[11,2, 4],
[4, 5 ,6],
[10, 8, -12]]
leftdia=0
rightdia=0
absv=0
for i in range(len(ma[0])):
    leftdia+=ma[i][i]
    rightdia+=ma[i][len(ma[0])-i-1]
absv=abs(leftdia-rightdia)
print(leftdia)
print(rightdia)
print(absv)
