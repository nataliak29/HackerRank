n=10
score=[3, 4 ,21 ,36 ,10 ,28 ,35, 5, 24 ,42]
highest=score[0]
lowest=score[0]
count_high=0
count_low=0

for i in range(n):
    if score[i]>highest:
        highest=score[i]
        count_high+=1
    elif score[i]< lowest:
        lowest=score[i]
        count_low+=1

print(count_high,count_low)
