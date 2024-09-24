s=input()#Accepted
l=0
r=len(s)-1
indexA=0
indexZ=0
while l<len(s):
    if s[l]=='A':
        indexA=l
        break 
    l+=1

while r>0:
    if s[r]=='Z':
        indexZ=r 
        break 
    r-=1 

print(indexZ-indexA+1)
        
