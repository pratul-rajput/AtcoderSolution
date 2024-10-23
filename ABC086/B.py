import math#accepted
a,b=input().split()
num=math.sqrt(int(a+b))
if num%1==0:
    print("Yes")
else:
    print("No")