#Accepted
x=int(input())
quot=x//11
rem=x%11
if rem==0:
    print(quot*2)
elif rem<=6:
    print(quot*2+1)
else:
    print(quot*2+2)