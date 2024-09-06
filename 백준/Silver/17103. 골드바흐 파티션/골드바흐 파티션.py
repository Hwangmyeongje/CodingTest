import math
import sys
input = sys.stdin.readline
t = int(input())

def sieve(limit):
    isPrime = [True] * (limit+1)
    isPrime[0] = isPrime[1] = False
    for i in range(2,int(math.sqrt(limit))+1):
        if isPrime[i]:
            for j in range(i*i,limit+1,i):
                isPrime[j] = False
    return isPrime

max_n = 0
cases= []
for i in range(t):
    n = int(input())
    cases.append(n)
    max_n = max(max_n,n)

isPrime = sieve(max_n)

for n in cases:
    cnt = 0
    for x in range(2, n//2 +1):
        y = n-x
        if isPrime[x] and isPrime[y]:
            cnt += 1

    print(cnt)
