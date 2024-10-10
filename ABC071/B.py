s=input()#accepted
s=sorted(s)

flag=None
for ch in range(ord('a'),ord('z')+1):
    if chr(ch) not in s:
        flag=chr(ch)
        break
print(flag)