#Accepted
o=input()
e=input()
s=""

for i,j in zip(o,e):
    s+=i
    s+=j

if len(o)>len(e):
    print(s+o[-1])
else:
    print(s)