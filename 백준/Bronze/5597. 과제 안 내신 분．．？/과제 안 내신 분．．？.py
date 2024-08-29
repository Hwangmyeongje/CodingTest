import sys
input = sys.stdin.readline


arr = []
for i in range(28):
   arr.append(int(input()))
arr.sort()
for i in range(1,31):
    if i not in arr:
        print(i)