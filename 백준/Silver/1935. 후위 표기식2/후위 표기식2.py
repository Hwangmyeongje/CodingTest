n = int(input())
oper = list(input())
num=[]
for i in range(n):
    num.append(int(input()))
stack =[]
for i in oper:
    if i.isalpha():
        stack.append(num[ord(i)-ord('A')])
    else:
        s2= stack.pop()
        s1 = stack.pop()
        if i == '+':
            stack.append(s1+s2)
        elif i == '-':
            stack.append(s1-s2)
        elif i == '*':
            stack.append(s1*s2)
        elif i == '/':
            stack.append(s1/s2)
print('%.2f' %stack[0])
