# 시간초과
# binary = input()
# ten_num =0
# for i in range(len(binary)):
#     ten_num += int(binary[len(binary)-1-i])*(2**i)
#
# oct_num = ''
# while ten_num != 0:
#     oct_num += str(ten_num % 8)
#     ten_num = ten_num //8
#
# print(oct_num[::-1])

binary = input()
if binary == '0' or set(binary) == {'0'}:
    print(0)
#이진수를 3자리씩 묶기 위해서 3의 배수로 길이를 맞춰서 해줌
else:
    if len(binary) % 3 !=0:
        binary = '0' * (3-len(binary) % 3) + binary
    oct_num = ''
    for i in range(0,len(binary),3):
        oct_digit = binary[i:i+3]
        a=int(oct_digit[0]) * 4
        b=int(oct_digit[1]) * 2
        c=int(oct_digit[2]) * 1
        oct_num += str(a+b+c)
    print(oct_num)