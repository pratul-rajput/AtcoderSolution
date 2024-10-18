X,Y=input().split()#best solution
if X>Y:
  print(">")
elif X==Y:
  print("=")
else:
  print("<")










x,y=input().split()#accepted,my solution
dict={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

if dict[x]<dict[y]:
    print("<")
elif dict[x]>dict[y]:
    print(">")
else:
    print("=")


