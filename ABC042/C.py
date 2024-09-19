import itertools
N,k=map(int,input().split())
disCoin=list(map(int,input().split()))
digits=[]
for i in range(10):
    if i not in disCoin:
        digits.append(i)

permutation=itertools.product(digits,repeat=4)
lists=[]
for perm in permutation:
    if perm[0]!=0:
        lists.append(int(''.join(map(str,perm))))

lists.sort()
for ele in lists:
    if N<ele:
        print(ele)
        break