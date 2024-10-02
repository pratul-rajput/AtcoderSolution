#Accepted,myself
w,a,b=map(int,input().split())
tup1=(a,a+w)
tup2=(b,b+w)
if b in range(tup1[0],tup1[1]+1) or b+w in range(tup1[0],tup1[1]+1):
    print(0)
elif b+w <a:
    print(a-(b+w))
else:
    print(b-(a+w))