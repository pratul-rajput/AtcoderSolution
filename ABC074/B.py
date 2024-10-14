n=int(input())#Accepted
k=int(input())
lst=list(map(int,input().split()))
result=0
for i in range(n):
    result+=min(lst[i]*2,abs(lst[i]-k)*2)
print(result)