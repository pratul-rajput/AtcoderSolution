x,y=map(int,input().split())
count=0
t=x
while t<=y:
    count+=1
    t=t*2
print(count)
