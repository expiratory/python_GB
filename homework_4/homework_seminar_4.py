# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# import random as r

# while True:
#     try:
#         n = int(input('Введите число n: '))
#         m = int(input('Введите число m: '))
#         if n > 0 and m > 0:
#             def fill_random_array(x):
#                 array_x = []
#                 for i in range(0, x):
#                     array_x.append(r.randint(0, 10))
#                 return array_x
#             array_n = fill_random_array(n)
#             array_m = fill_random_array(m)
#             print(array_n)
#             print(array_m)
#             final_array = []
#             for i in range(0, n):
#                 for j in range(0, m):
#                     if array_n[i] == array_m[j]:
#                         final_array.append(array_n[i])
#             final_result = set(final_array)
#             print(final_result)
#             break
#         else:
#             print('Значения n и m отрицательными или нулевыми быть не могут, попробуйте еще раз')
#     except:
#         print('Некорректный ввод, попробуйте еще раз')

# Задача 24: Про сбор черники)

import random as r

while True:
    try:
        n = int(input('Введите число n: '))
        if n > 0:
            def fill_random_array(x):
                array_x = []
                for i in range(0, x):
                    array_x.append(r.randint(1, 5))
                return array_x
            array_n = fill_random_array(n)
            print(array_n)
            result_array = []
            for i in range(0, n):
                result_array.append(array_n[i-2]+array_n[i-1]+array_n[i])
            max = 0
            for j in result_array:
                if j > max:
                    max = j
            print(max)
            break
        else:
            print('Значение n отрицательным или нулевым быть не может, попробуйте еще раз')
    except:
        print('Некорректный ввод, попробуйте еще раз')