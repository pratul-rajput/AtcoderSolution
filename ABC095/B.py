n,x=map(int,input().split())#accepted
lst=[]
for i in range(n):
    lst.append(int(input()))

rem=x-sum(lst)
print((rem//min(lst))+n)