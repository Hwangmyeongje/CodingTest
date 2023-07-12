bracket = input()
cnt = 0
pre = ')'
stack = []
for i in bracket:
    if i == '(':
        stack.append(i)
    elif i ==')' and pre == '(': #레이저인 경우
        stack.pop()
        cnt += len(stack) #쇠막대기를 겹쳐져 있던 것들 모두 추가 해줌
    else: #쇠막대기 오른쪽 끝을 의미
        stack.pop()
        cnt +=1
    pre = i
print(cnt)
