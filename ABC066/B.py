s=list(input())
for i in range(s):
    s.pop()
    if i%2!=0:
        pass 
    else:
        half=lens(s)//2
        t=s[:half]+s[half:]
        if s==t:
            print(len(s))
            break

    
