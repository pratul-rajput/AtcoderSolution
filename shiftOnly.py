#https://qiita.com/drken/items/fd4e5e3630d0f5859067#5-%E9%81%8E%E5%8E%BB%E5%95%8F%E7%B2%BE%E9%81%B8-10-%E5%95%8F

n=int(input())
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
