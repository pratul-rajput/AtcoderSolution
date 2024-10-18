n=int(input())
num1=2
num2=1
if n==1:
    fib=1
for i in range(1,n):
    fib=num1+num2
    num1=num2
    num2=fib 
print(fib)