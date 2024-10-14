n=int(input())#accepted,my solution
map={}
for i in range(n):
    num=int(input())
    if num in map:
        map[num]=map.get(num,0)-1
        if map[num]<=0:
            del map[num]
    else:
        map[num]=1+map.get(num,0) 

print(sum(map.values()))

"""
# Better Solution with logic 
from collections import defaultdict

n = int(input())
seqA = [int(input()) for _ in range(n)]

written = defaultdict(int)
for a in seqA:
    written[a] += 1

cnt = 0
for k, v in written.items():
    if v % 2 == 1:
        cnt += 1
print(cnt)

"""