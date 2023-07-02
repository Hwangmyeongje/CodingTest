n= int(input())
stack,oper =[],[]
flag = 1
cnt =1
for i in range(n):
   num = int(input())
   while cnt<=num:
       stack.append(cnt)
       oper.append('+')
       cnt +=1
   if stack[-1] == num:
       stack.pop()
       oper.append('-')
   else:
       flag = 0
       break
if flag == 0:
    print("NO")
else:
    for i in oper:
        print(i)