# Задача про факториал

# def true_number():
#     num = int(input('Введите целое неотрицательное число N: '))
#     while num < 0:
#         num = int(input('Вы ввели число меньше нуля, попробуйте еще раз: '))
#     else:
#         return num

# def factorial(number):
#     i = 1
#     factorial = 1
#     while i <= number:
#         factorial *= i
#         i += 1
#     print(factorial)

# n = true_number()
# factorial(n)

# Задача про число Фибоначчи

# def true_number():
#     num = int(input('Введите число N: '))
#     while num < 0:
#         num = int(input('Вы ввели число меньше нуля, попробуйте еще раз: '))
#     else:
#         return num

# def fibonacci(number):
#     if number == 0: return 1
#     if number == 1: return 2
#     number0 = 0
#     number1 = 1
#     temp = 0
#     count = 2
#     while number>=number1:
#         if number == number1: return count
#         temp = number1
#         number1 += number0
#         number0 = temp
#         count += 1
#     return -1

# n = true_number()
# fib = fibonacci(n)
# print(fib)

# Задача про самую длинную оттепель

# import random

# n = 100
# m = []
# count = 0
# max = 0
# for i in range(0,n):
#     random_number = round(random.uniform(-50,50),0)
#     m.append(random_number)
#     if m[i] > 0:
#         count += 1 
#         temp = count
#     if m[i] < 0:
#         count = 0
#     if temp > max: max = temp

# print(m)
# print(max)

# Задача про мужика, тещу, арбузы

import random

n = 10
watermellons = []
for i in range(0,n):
    random_number = round(random.uniform(5000,30000))
    watermellons.append(random_number)
print(watermellons)

min = max = watermellons[0]
for item in watermellons:
    if item>max: max = item
    if item<min: min = item
print(min, max)