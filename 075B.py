h,w=list(map(int,input().split()))
matrix=[list(input()) for _ in range(h)]
directions=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
for i in range(h):
    for j in range(w):
        
        if matrix[i][j]==".":
           count=0
           for dr,dc in directions:
               if i+dr in range(h) and j+dc in range(w) and matrix[i+dr][j+dc]=="#":
                  count+=1 
           matrix[i][j]=str(count)

for row in matrix:
    print("".join(row))
   
                         

