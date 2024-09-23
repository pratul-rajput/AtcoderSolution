n=int(input())
string=input()
global_max=0
maxs=0
for ch in string:
    if ch=="I":
        maxs+=1
        global_max=max(maxs,global_max)
    else:
        maxs-=1
print(global_max)