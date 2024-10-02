h,w=map(int,input().split())
matrix=['#'*(w+2)]
for i in range(h):
    matrix.append('#'+input()+'#')
matrix.append('#'*(w+2))
for row in matrix:
    print(row)
