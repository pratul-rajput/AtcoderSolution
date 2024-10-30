n=int(input())
s=[]
for i in range(n):
    s.append(input())

c=[0,0,0,0,0]
for i in range(n):
    if s[i][0]=="M":
        c[0]+=1
    if s[i][0]=="A":
        c[1]+=1
    if s[i][0]=="R":
        c[2]+=1
    if s[i][0]=="C":
        c[3]+=1
    if s[i][0]=="H":
        c[4]+=1
ans=0

for i in range(len(c)):
    for j in range(i+1,len(c)):
        for k in range(j+1,len(c)):
            ans+=c[i]*c[j]*c[k]
print(ans)