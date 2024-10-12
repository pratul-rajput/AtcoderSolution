n=int(input())#accepted
lst=[tuple(map(int,input().split())) for _ in range(n)]
result=0
for tup in lst:
    c=tup[1]-tup[0]+1
    result+=c

print(result)