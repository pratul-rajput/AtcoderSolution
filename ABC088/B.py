n=int(input())
lst=list(map(int,input().split()))
lst.sort(reverse=True)
a,b=0,0
for i in range(len(lst)):
    if i%2==0:
        a+=lst[i]
    else:
        b+=lst[i]
print(a-b)

