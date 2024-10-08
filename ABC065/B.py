n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))

st1=set(lst)
st2=set()
count=0
for el in lst:
    if el not in st1:
        st2.add(el)
        count+=1
    else:
        break 
if st1!=st2:
    print("-1")
else:
    print(count)