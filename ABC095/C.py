a,b,c,x,y=map(int,input().split())#accepted
separate=a*x+b*y
mn=min(x,y)
val=a if x>y else b 
rem=x-y if x>y else y-x
ans1=c*min(x,y)*2+rem*val 
ans2=max(x,y)*c*2
print(min(separate,ans1,ans2))