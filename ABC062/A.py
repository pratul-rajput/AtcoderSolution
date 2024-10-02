list1=[1,3,5,7,8,10,12]
list2=[4,6,9,11]
x,y=map(int,input().split())
if x in list1 and y in list1:
    print("Yes")
elif x in list2 and y in list2:
    print("Yes")
else:
    print("No")