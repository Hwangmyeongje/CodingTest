n = int(input())
arr = [0 for _ in range(10)]
while n > 0:
    check = n%10
    #6과 9 중 더 작은 인덱스번째를 증가 시킨다.
    if check == 6 or check ==9:
        if arr[6] <= arr[9]:
            arr[6] +=1
        else:
            arr[9] +=1
    else:
        arr[check] +=1
    n //= 10
print(max(arr))


