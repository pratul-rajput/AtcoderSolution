x,a,b=map(int,input().split())
best_by=a 
if 0<=b<=a:
    print("delicious")
elif a<b<=(a+x):
    print("safe")
else:
    print("dangerous")