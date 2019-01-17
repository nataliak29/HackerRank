n=44
grades=[84,94,21,0,18,100,18,62,30,61,53,0,43,2,29,53,61,40,14,4,29,98,37,23,46,9,79,62,20,38,51,99,59,47,4,86,61,68,17,45,6,1,95,95]
finalgrades=[]

for g in grades:
    if g<38:
        finalgrades.append(g)
    elif g%5==4:
        finalgrades.append(g+1)
    elif g%5==3:
        finalgrades.append(g+2)
    else: finalgrades.append(g)
print(finalgrades)
