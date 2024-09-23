n,m=map(int,input().split())
named_taro=set()

for _ in range(m):
    a,b=input().split()
    if int(a) not in named_taro and b!="F":
        print("Yes")
        named_taro.add(int(a))
    else:
        print("No")
