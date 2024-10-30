from collections import defaultdict
blue = defaultdict(int)
red = defaultdict(int)

n = int(input())
for _ in range(n): blue[input()]+=1
m = int(input())
for _ in range(m): red[input()]+=1
ans=0
for k,v in blue.items():
    ans=max(ans,v-red[k])
print(ans)


# from collections import defaultdict
# n=int(input())
# blue=[input() for i in range(n)]
# m=int(input())
# red=[input() for j in range(m)]
# dict = defaultdict(lambda: [0, 0])
# for st in blue:
#     dict[st][0]+=1
# for st in red:
#     dict[st][1]+=1
# mx=0
# for x,y in dict.values():
#     mx=max(mx,x-y)
# print(mx)