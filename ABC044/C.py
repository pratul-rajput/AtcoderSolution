n,a=map(int,input().split())
num_list=list(map(int,input().split()))
prefix_sum=[0]*n 
count=0
for i in range(1,n):
    if num_list[i]==a:
        count+=1  
    prefix_sum[i]=prefix_sum[i-1]+num_list[i]
    if prefix_sum[i]/(i+1)==a:
        count+=1 
    for j in range(i):
        if (prefix_sum[i]-num_list[j])/(i)==a:
            count+=1 
print(count)
    

