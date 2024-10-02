a,b,c=map(int,input().split())
i=1
traced=set()
while True:
    rem=(a*i)%b 
    if rem==c:
        print("YES")
        break 
    if rem in traced:
        print("NO")
        break
    traced.add(rem)
    i+=1