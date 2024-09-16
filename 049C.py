s=input()
while s:
    query=["dreamer","dream","eraser","erase"]
    for i in query:
        if s.endswith(i):
            s=s[:-len(i)]
            break
    else:
        print("NO")
        exit() 
print("YES")