n,y=map(int,input().split())
p,q,r=-1,-1,-1
for i in range(n+1):
    for j in range(n+1-i):
        k=n-i-j 
        if  i*10000+j*5000+k*1000==y:
            p,q,r=i,j,k 

print(f"{p} {q} {r}")