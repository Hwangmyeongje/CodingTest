t= int(input())
for _ in range(t):
    r,s=input().split()
    r = int(r)
    s2=[]
    for i in range(len(s)):
        for _ in range(r):
            s2.append(s[i])
    for j in range(len(s)* r):
        print(s2[j],end='')
    print()
