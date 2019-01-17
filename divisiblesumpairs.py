#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
n=6
k=3
ar=[1,3,2,6,1,2]

def divisibleSumPairs(n, k, ar):
    number_of_pairs=0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if (ar[i]+ar[j] )%k==0:
                number_of_pairs+=1

    return number_of_pairs

print(divisibleSumPairs(n, k, ar))
