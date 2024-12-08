import sys
a,b,x=map(int,input().split())
if a>x:
    print("NO")
    sys.exit()
if x-a<=b:
    print("YES")
else:
    print("NO")