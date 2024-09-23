n,q=map(int,input().split())
s=input()
query=[]
def sliding_window(ss):
    count=0
    start=0
    end=0
    while end<len(ss):
        if (end-start+1)==3:
            if ss[start:end+1]=="ABC":
                count+=1
            start+=1
        end+=1
    return count
for i in range(q):
    x,c=input().split()
    query.append((int(x),c))

lists=list(s)
for x,c in query:
    lists[x-1]=str(c)
    p=''.join(lists)
    print(sliding_window(p))


