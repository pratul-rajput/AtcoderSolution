n,k=map(int,input().split())
count=0
for i in range(n):
    cur,b=map(int,input().split())
    count+=b
    if count>=k:
        print(cur)
        break