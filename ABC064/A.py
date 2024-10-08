inp=list(map(int,input().split()))
if (inp[-2]*10+inp[-1])%4==0:
    print("YES")
else:
    print("NO")