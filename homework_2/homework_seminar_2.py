# Задача 10 На столе лежат n монеток. Некоторые
# из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх
# одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# import random as r

# while True:
#     try:
#         n = int(input('Введите число n: '))
#         if n > 0:
#             array = []
#             for item in range(0, n):
#                 array.append(r.randint(0, 1))
#             print(array)
#             count0 = 0
#             count1 = 0
#             for i in array:
#                 if i == 0:
#                     count0 += 1
#                 else:
#                     count1 += 1
#             if count0 < count1:
#                 print('Надо перевернуть', count0, 'монет')
#             else:
#                 print('Надо перевернуть', count1, 'монет')
#             break
#         else:
#             print('Отрицательного количества монет быть не может, попробуйте еще раз')
#     except:
#         print('Некорректный ввод, попробуйте еще раз')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


# x = r.randint(1, 1000)
# y = r.randint(1, 1000)
# s = x + y
# p = x * y
# print('Петя загадал два числа от 1 до 1000, их сумма равна',
#       s, 'и их произведение равно', p)

# for i in range(1, 1000):
#     if (s-i) == (p/i):
#         break

# y_find = i
# x_find = s - i

# print('Катя отгадала два числа, это', x_find, 'и', y_find)


#  Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2 в степени k), не превосходящие числа N.

while True:
    try:
        n = int(input('Введите число n: '))
        if n > 0:
            i = 1
            k = 0
            while i < n:
                i = 2**k
                if (i > n):
                    break
                print(i)
                k += 1
            break
        else:
            print('Число n не должно быть отрицательным, попробуйте еще раз')
    except:
        print('Некорректный ввод, попробуйте еще раз')