import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    cnt =0
    while n>0:
        if n % 2 == 1:
          arr.append(cnt)
        n //= 2
        cnt += 1
    print(' '.join(map(str,arr)))

