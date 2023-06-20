def solution(s):
    zero = 0
    cnt = 0
    while s !='1':
        if '0' in s: 
            zero += s.count('0')
            s = s.replace('0','') #공백으로 바꾸기
            
        s = bin(len(s))[2:] #2진수로 변환
        cnt +=1
    return [cnt,zero]