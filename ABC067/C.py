n=int(input())
lst=list(map(int,input().split()))
start,end=0,sum(lst)
global_min=float('inf')
for i in range(n-1):
    start+=lst[i]
    end-=lst[i]
    global_min=min(global_min,abs(start-end))

print(global_min)
#accepted






'''
Alternate Solution
from sys import stdin
input = lambda: stdin.readline().rstrip("\n")

n = int(input())
a = list(map(int, input().split()))

start, end = 0, sum(a)
minimum = 10 ** 18
for i in range(n-1):
    start += a[i]
    end -= a[i]
    minimum = min(minimum, abs(end - start))

print(minimum)
'''