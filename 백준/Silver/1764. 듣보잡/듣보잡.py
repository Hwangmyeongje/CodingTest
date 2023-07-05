import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a,b= set(),set()
for _ in range(n):
    a.add(input().rstrip())
for _ in range(m):
    b.add(input().rstrip())
cnt = 0
c = set()
for i in a:
    if i in b:
        cnt +=1
        c.add(i)
c = sorted(c)
print(cnt)
for i in c:
    print(i)