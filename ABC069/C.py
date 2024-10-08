n=int(input())#accepted
A=list(map(int,input().split()))
if n==2:
    if A[0]*A[1]%4==0:
       print("Yes")
    else:
        print("No")
else:
    odd=0
    even=0
    four=0
    for i in A:
        if i%4==0:
            four+=1
        elif i%2==0:
            even+=1
        else:
            odd+=1

    if odd==0:
        print("Yes")
    elif four==odd-1 and even==0:
        print("Yes")
    else:
        print("No")





'''
User:oikot
--------------------
N = int(input())
A = list(map(int, input().split()))

if N == 2:
    if (A[0]*A[1]) % 4 == 0:
        print("Yes")
    else:
        print("No")
    exit()
else:
    odd = 0
    even = 0
    fours = 0
    for a in A:
        if a % 4 == 0:
            fours += 1
        elif a % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0:
        print("Yes")
    elif fours >= odd:
        print("Yes")
    elif fours == odd - 1 and even == 0:
        print("Yes")
    else:
        print("No")
    
'''