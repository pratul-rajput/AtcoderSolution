a,b=map(int,input().split())
def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev 
count=0
for i in range(a,b+1):
    if i==reverse(i):
        count+=1
print(count)