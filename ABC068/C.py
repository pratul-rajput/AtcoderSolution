n,m=map(int,input().split())#Accepted
lst=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    lst[a].append(b)
    lst[b].append(a)
judge=False
for i in lst[0]:
    if n-1 in lst[i]:
        judge=True 

if judge:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
    