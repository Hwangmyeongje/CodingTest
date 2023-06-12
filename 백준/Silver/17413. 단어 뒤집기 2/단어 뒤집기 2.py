from collections import deque

s = input()
deq = deque()  # 문자를 저장하기 위한 덱
result = deque()  # 결과를 저장하기 위한 덱
inside_tag = False  # 태그 내부 여부를 확인하기 위한 변수

for char in s:
    if char == '<':
        inside_tag = True  # 태그 내부에 진입
        while deq:
            result.append(deq.pop())  # 현재까지 저장된 문자를 뒤집어서 결과에 추가
        result.append(char)  # '<' 문자를 결과에 추가
    elif char == '>':
        inside_tag = False  # 태그 내부에서 벗어남
        result.append(char)  # '>' 문자를 결과에 추가
    elif char == ' ':
        if inside_tag:
            result.append(char)  # 태그 내부에서는 공백을 그대로 결과에 추가
        else:
            while deq:
                result.append(deq.pop())  # 공백을 만나면 현재까지 저장된 문자를 뒤집어서 결과에 추가
            result.append(char)  # 공백 문자를 결과에 추가
    else:
        if inside_tag:
            result.append(char)  # 태그 내부에서는 문자를 그대로 결과에 추가
        else:
            deq.append(char)  # 그 외의 경우에는 문자를 저장

while deq:
    result.append(deq.pop())  # 마지막으로 남은 문자를 결과에 추가

for char in result:
    print(char, end='')
