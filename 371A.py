AB,AC,BC=input().split()

if (AB=="<" and AC==">" and BC==">") or (AB==">" and AC=="<" and BC=="<"):
  print("A")
elif (AB=="<" and AC=="<" and BC=="<") or (AB==">" and AC==">" and BC==">"):
  print("B")
else:
  print("C")