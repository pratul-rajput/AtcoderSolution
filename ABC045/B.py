dicts={"a":list(input()),"b":list(input()),"c":list(input())}
turn="a"
while dicts[turn]:
    turn=dicts[turn].pop(0)

print(turn.upper())



















# Sa=input()
# Sb=input()
# Sc=input()
# saList=list(Sa)[::-1]
# sbList=list(Sb)[::-1]
# scList=list(Sc)[::-1]
# name="A"
# while True:
#     if name=="A":
#         if len(saList)==0:
#             break
#         popele=saList.pop()
#     elif name=="B":
#         if len(sbList)==0:
#             break
#         popele=sbList.pop()
#     elif name=="C":
#         if len(scList)==0:
#             break
#         popele=scList.pop()
#     name=popele.upper()
# print(name)
 