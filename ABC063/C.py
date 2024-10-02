#Accepted
n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
lst.sort()
sm=sum(lst)
if sm%10!=0:
    print(sm)
else:
    flag=0
    for ele in lst:
         if (sm-ele)%10!=0:
            flag=sm-ele
            break
 
    print(flag)

"""
Alternat Solution

n=int(input())
x=0
y=10000000
for i in range(n):
    a=int(input())
    x+=a
    if a%10!=0:
        y=min(a,y)
if y==10000000:
    print(0)
elif x%10!=0:
    print(x)
else:
    print(x-y)

"""