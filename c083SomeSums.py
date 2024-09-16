lists=list(map(int,input().split()))

sumss=0
def digitSum(num):
    sums=0
    while num!=0:
        rem=num%10
        sums+=rem
        num//=10
    return sums
for i in range(1,lists[0]+1):
    x=digitSum(i)
    if x  in range(lists[1],lists[2]+1):
        sumss+=i
print(sumss)
