
n=input()
x=sum([int(i) for i in n])
if int(n)%x==0:
    print("Yes")
else :
    print("No")



"""n=int(input())
if n<10:
    print("Yes")
    exit()
def sums(n):
    sumss=0
    while n>0:
        rem=n%10
        sumss+=rem 
        n=n//10
    return sumss
if n%sums(n)==0:
    print("Yes")
else:
    print("No")
"""