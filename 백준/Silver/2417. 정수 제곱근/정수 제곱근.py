n = int(input())
start = 0
#2^63의 제곱근을 end로 설정
end = 30370005000
flag = False
sol = 0
while start<end:
    mid = (start + end)//2
    if mid **2 == n:
        sol = mid
        flag =True
        break
    elif mid **2 <n:
        start = mid +1
    else:
        end = mid -1
#end가 n의 제곱근보다 작은 가장 큰 정수,
if not flag:
    if end * end <n:
        sol = end +1
    else: sol =end
print(sol)
