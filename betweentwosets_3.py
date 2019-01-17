a=[2,4]
b=[16,32,96]

def getTotalX(a, b):
    count=0
    for i in range(max(a),max(b)+1):
        if sum(i%ai for ai in a)+sum(bi%i for bi in b)==0:
            count+=1
    return count

print(getTotalX(a, b))
