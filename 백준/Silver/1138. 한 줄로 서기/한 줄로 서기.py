n = int(input())
arr = list(map(int, input().split()))

line = [0] * (n)

for i in range(n):
    count = 0
    for j in range(n):
        if line[j] == 0 and count == arr[i]:
            line[j] = i+1
            break
        elif line[j] == 0:
            count += 1

for i in range(n):
    print(line[i], end=' ')
