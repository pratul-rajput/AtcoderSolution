#Accepted
n,m=map(int,input().split())
if n>=m:
    print(m//2)
else:
    print(n+(m-n*2)//4)
