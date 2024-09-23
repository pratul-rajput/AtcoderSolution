n=int(input())
T=list(map(int,input().split()))
M=int(input())
drinks=[]
for i in range(M):
    index,value=map(int,input().split())
    drinks.append((index,value))
totalSum=sum(T)
for index,value in drinks:
    print(totalSum-T[index-1]+value)

