n=int(input())#accepted
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