r1=list(input())#ACCEPTED BUT COMPLICATED
r2=list(input())
matrix=[r1,r2]
if matrix[0][0]==matrix[1][2] and matrix[0][1]==matrix[1][1] and matrix[0][2]==matrix[1][0]:
    print("YES")
else:
    print("NO")


'''
a=input()
b=input()
if a[0]==b[2] and a[1]==b[1] and a[2]==b[0]:
  print('YES')
else:
  print('NO')
'''