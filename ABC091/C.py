n=int(input())
red=[tuple(map(int,input().split())) for _ in range(n)]
blue=[tuple(map(int,input().split())) for _ in range(n)]
count=0
st=set()
for i in range(n):
    for j in range(n):
        if j not in st and blue[i][0]>red[j][0] and blue[i][1]>red[j][1]:
            count+=1
            st.add(j)
print(count)

