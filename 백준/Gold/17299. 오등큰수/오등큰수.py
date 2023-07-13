from collections import Counter

n = int(input())
arr = list(map(int,input().split()))
result = [-1] * n
cnt = Counter(arr)
stack = []
for i in range(n):
    while stack and cnt[arr[stack[-1]]] < cnt[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)