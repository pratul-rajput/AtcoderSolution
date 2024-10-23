n,a,b=map(int,input().split())
sms=0
def digitSum(n):
    sm=0
    while n>0:
        rem=n%10
        sm+=rem
        n//=10
    return sm 
for i in range(1,n+1):
    if digitSum(i) in range(a,b+1):
        sms+=i
print(sms)


