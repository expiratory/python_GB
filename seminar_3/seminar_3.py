#Задача - вывести из масиива элементы так, чтобы они не повторялись

#  import random as r

# while True:
#     try:
#         n = int(input('Введите число n: '))
#         if n > 0:
#             array = []
#             for item in range(0, n):
#                 array.append(r.randint(0, 10))
#             print(array)
#             array_to_set = set(array)
#             print(array_to_set)
#             break
#         else:
#             print('Отрицательного количества элементов массива быть не может, попробуйте еще раз')
#     except:
#         print('Некорректный ввод, попробуйте еще раз')


# Задача на сдвиг массива

# import random as r

# while True:
#     try:
#         n = int(input('Введите число n: '))
#         k = int(input('Введите число k: '))
#         if n > 0 and k > 0:
#             array = []
#             for item in range(0, n):
#                 array.append(r.randint(0, 10))
#             print(array)
#             while k > 0:
#                 elem = array.pop()
#                 array.insert(0, elem)
#                 k -= 1
#             print(array)
#             break
#         else:
#             print('Значения n и k отрицательными или нулевыми быть не могут, попробуйте еще раз')
#     except:
#         print('Некорректный ввод, попробуйте еще раз')

# Задача с уникальными значениями в словаре

dict = \
    {
        'I' : 'S001',
        'II' : 'S002',
        'III' : 'S001',
        'IV' : 'S005',
        'V' : 'S005',
        'VI' : 'S009',
        'VII' : 'S007'
    }

result = []
for v in dict.values():
    result.append(v)
print(result)
res = set(result)
print(res)