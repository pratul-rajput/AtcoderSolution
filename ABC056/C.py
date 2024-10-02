x=int(input())
ans=0
t=0
while True:
  t+=1
  ans+=t
  if ans>=x:
    break
print(t)