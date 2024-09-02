import sys
input = sys.stdin.readline

max = 0
total = 0
for i in range(10):
    get_off,get_on = map(int,input().split())
    total = total + get_on - get_off
    if max < total:
        max = total
print(max)