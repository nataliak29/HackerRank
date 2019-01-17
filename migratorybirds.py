arr=[4,1, 2, 3, 5, 4 ,3 ,2, 1, 3, 4]

def migratoryBirds(arr):
    birds={}
    for bi in arr:
        try:
            birds[bi]+=1
        except: birds[bi]=1
    maxval=max(birds.values())
    birdkey=min([k for k,v in birds.items() if v==maxval])

    return birdkey


print(migratoryBirds(arr))
