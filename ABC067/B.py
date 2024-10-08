n,k=map(int,input().split())
stick=list(map(int,input().split()))
stick.sort()
print(sum(stick[-k:]))
#accepted