import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr = list(map(int,input().split()))

output =0
for i in range(k):
    output += arr[i]
sum = output
left = 0
right = k-1
while True:
    sum -= arr[left]
    left += 1
    right += 1
    if right == n:
        break
    sum += arr[right]
    if sum > output:
        output = sum


print(output)

