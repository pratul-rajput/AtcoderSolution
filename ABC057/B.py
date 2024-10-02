n,m=map(int,input().split())
student = [tuple(map(int,input().split())) for _ in range(n)]
checkpoint= [tuple(map(int,input().split())) for _ in range(m)]
for stud in student:
    min_dist=float('inf')
    index=-1
    for i,checkp in enumerate(checkpoint):
        dist=abs(stud[0]-checkp[0])+abs(stud[1]-checkp[1])
        if dist<min_dist:
            min_dist=dist
            ind=i+1
    print(ind)
