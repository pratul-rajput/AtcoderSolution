#source:editorial user:aprilhare submission#57929566
#chatgpt also
#Accepted
n,m=map(int,input().split())
A=[input() for _ in range(n)]
B=[input() for _ in range(m)]

for ar in range(n-m+1):
    for ac in range(n-m+1):
        match=True 
        for i in range(m):
            for j in range(m):
                if A[ar+i][ac+j]!=B[i][j]:
                    match=False
                    break
        if match:
            break 
    if match:
        break 

print("Yes" if match else "No") 

