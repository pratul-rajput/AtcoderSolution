n=int(input())#accepted
lists=[list(map(int,input().split())) for _ in range(n)]

t_x=0
t_y=0
t_t=0
can=True 
for t,x,y in lists:
    dt=t-t_t 
    dist=abs(x-t_x)+abs(y-t_y)
    if dist>dt: 
        can=False 
    if dist%2!=dt%2:
        can=False 
    t_t,t_x,t_y=t,x,y

if can:
    print("Yes")
else:
    print("No")
    