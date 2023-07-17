s = list(input())
stack = []
result = []
for i in s:
    if i.isalpha():
        result.append(i)
    else:
        if i =='(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result.append(stack.pop())
            stack.append(i)
        elif i== '+' or i == '-':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
while stack:
    result.append(stack.pop())
print(''.join(result))
