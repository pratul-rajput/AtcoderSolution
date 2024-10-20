import math
a,b=map(int,input().split())
avg=(a+b)/2
if avg-int(avg)<int(avg)+1-avg:
    print(math.floor(avg))
else:
    print(math.ceil(avg))