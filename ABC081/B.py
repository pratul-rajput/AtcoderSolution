n=int(input())#accepted
lists=list(map(int,input().split()))
flag=0
count=0
while True:
    for i in range(len(lists)):
        if lists[i]%2!=0:
            flag=1
        else:
            lists[i]/=2 
    if flag==1:
        print(count)
        break
    count+=1