n = int(input())
for _ in range(n):
    string = list(input().split())
    for i in string:
        print(i[::-1], end=' ')