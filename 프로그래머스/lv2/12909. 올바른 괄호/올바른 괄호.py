from collections import deque
def solution(s):
    answer = True
    deq = deque()
    for i in s:
        if i == ')' and '(' not in deq:
            return False
        elif i== ')' and '(' in deq:
            deq.pop()
        print(i)
        if i == '(':
            deq.append(i)
    if len(deq) != 0:
        return False
    return True