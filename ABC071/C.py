n=int(input()) #accepted,important
lst=list(map(int,input().split()))
lst.sort(reverse=True)
i=1
res=[]
while i<n:
    if lst[i-1]==lst[i]:
        res.append(lst[i])
        i+=2
    else:
        i+=1
    
    if len(res)==2:
        break 

if len(res)==2:
   print(res[0]*res[1])
else:
    print(0)











'''
N = int(input())
A = list(map(int,input().split()))

hens = []
A.sort(reverse=True)

pairs = 0
i = 1
while i < N:
    if A[i-1] == A[i]:
        hens.append(A[i])
        i += 2    
    else:
        i += 1

    if len(hens) == 2:
        break



if len(hens) == 2:
    print(hens[0] * hens[1])
else:
    print(0)
'''