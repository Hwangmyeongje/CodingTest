t= int(input())
for _ in range(t):
    a=[]
    flag = 1
    s = list(input())
    for i in range(len(s)):
        if(s[i] == '('):
            a.append('(')
        else:
            if len(a) == 0:
                flag = 0
                break
            a.pop()
    if(len(a) == 0 and flag == 1):
        print("YES")
    else:
        print("NO")