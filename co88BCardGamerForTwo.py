n=int(input())
lists=list(map(int,input().split()))
lists.sort()
count1=0
count2=0
for i in range(len(lists)):
    if i%2==0:
        count1+=lists[i]
    else:
        count2+=lists[i]
print(abs(count1-count2))