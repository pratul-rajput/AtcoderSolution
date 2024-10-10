n=int(input())#accepted
lst=[int(input()) for _ in range(n)]

def hcf(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return abs(a*b)//hcf(a,b)

def lcm_of_list(numbers):
    result=numbers[0]
    for num in numbers[1:]:
        result=lcm(result,num)
    return result
print(lcm_of_list(lst))
