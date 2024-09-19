abc=input()
dicts={}
for ch in abc:
    dicts[ch]=1+dicts.get(ch,0)

flag=0
for i in dicts:
    if dicts[i]%2!=0:
        flag=1

if flag:
    print("No")
else:
    print("Yes")

        