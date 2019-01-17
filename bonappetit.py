n=4
k=1
bill=[3,10,2,9]
b=12

def bonAppetit(bill, k, b):
    totalbill=sum(bill[i] for i in range(len(bill)))
    if int(b-(totalbill -bill[k]) /2)==0:
        return "Bon Appetit"
    else:
        return int(b-(totalbill -bill[k]) /2)




print(bonAppetit(bill, k, b))
