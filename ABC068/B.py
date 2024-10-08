n=int(input())#Accepted
def divisorCounter(n):
    count=0
    while n%2==0:
        count+=1
        n=n//2
    return count
maxDiv=0
val=1
for i in range(1,n+1):
    if maxDiv<divisorCounter(i):
        maxDiv=divisorCounter(i)
        val=i 
print(val)