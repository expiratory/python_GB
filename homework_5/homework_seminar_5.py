# Задача 26: Программа возводитчисло A в целую степень B с помощью рекурсии

def grade(A, B, RES):
    if B > 0:
        RES *= A
        B -= 1
        grade(A, B, RES)
        if B == 0: print(RES)
    if B < 0:
        RES /= A
        B += 1
        grade(A, B, RES)
        if B == 0: print(RES)

while True:
    try:
        a = int(input('Введите число A: '))
        b = int(input('Введите число B: '))
        result = 1
        grade(a,b,result)
        break
    except:
        print('Некорректный ввод, попробуйте еще раз')

# Программа рекурсией находит сумму двух целых неотрицательных чисел

# def sum(A, B, CNT):
#     if A >= B:
#         if CNT <= B:
#             A += 1
#             CNT += 1
#             sum(A, B, CNT)
#         else:
#             print(A)
#     if A < B:
#         if CNT <= A:
#             B += 1
#             CNT += 1
#             sum(A, B, CNT)
#         else:
#             print(B)


# while True:
#     try:
#         a = int(input('Введите число A: '))
#         b = int(input('Введите число B: '))
#         if a > 0 and b > 0:
#             count = 1
#             sum(a,b,count)
#             break
#         else: print('A и B должны быть целыми неотрицательными числами')
#     except:
#         print('Некорректный ввод, попробуйте еще раз')