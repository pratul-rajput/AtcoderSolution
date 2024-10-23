n=int(input())
lst=(map(int,input().split()))
dict={}
result=0

for el in lst:
    dict[el]=1+dict.get(el,0)
for key in dict:
    if dict[key]==key:
        continue
    elif dict[key]>key:
        result+=dict[key]-key
    else:
        result+=dict[key]

print(result)

'''
from collections import defaultdict
N=int(input())
A=list(map(int,input().split()))

cnt=defaultdict(int)
for a in A:
    cnt[a]+=1
    
ans=0
for a in cnt:
    if cnt[a]==a:
        continue
    elif cnt[a]>a:
        ans+=cnt[a]-a
    else:
        ans+=cnt[a]
        
print(ans)
'''