import sys
input = sys.stdin.readline
stack = []
n = int(input())
for i in range(n):
    command = list(map(int,input().split()))
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    elif command[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)

