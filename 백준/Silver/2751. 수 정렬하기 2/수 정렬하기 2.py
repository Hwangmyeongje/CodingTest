import sys
input = sys.stdin.readline
n= int(input())
a=list()
for _ in range(n):
    a.append(int(input()))
a.sort()
for i in a:
    print(i)
