pay = int(input())
pay = 1000 - pay
n= 0
while pay >0:
    if pay >= 500:
        k = pay//500
        pay -= k *500
        n += k
    elif pay >= 100:
        k = pay//100
        pay -= k *100
        n += k
    elif pay >= 50:
        k = pay // 50
        pay -= k * 50
        n += k
    elif pay >= 10:
        k = pay // 10
        pay -= k * 10
        n += k
    elif pay >= 5:
        k = pay // 5
        pay -= k * 5
        n += k
    else:
        k = pay // 1
        pay -= k * 1
        n += k
print(n)