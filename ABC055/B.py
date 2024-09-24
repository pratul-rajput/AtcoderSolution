#Accepted
MOD=10**9+7
fact=1
n=int(input())
for i in range(1,n+1):
    fact*=i
    fact=fact%MOD 
print(fact)