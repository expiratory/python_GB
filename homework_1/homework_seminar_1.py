# Задача 2: Найдите сумму цифр трехзначного числа

# def true_number():
#     num = int(input('Введите трехзначное число: '))
#     while num < 99 or num > 1000:
#         num = int(input('Вы ввели не трехзначное число, попробуйте еще раз: '))
#     else:
#         return num


# def sum_of_digits(number):
#     sum = 0
#     while number > 9:
#         sum += number % 10
#         number //= 10
#     sum += number
#     return sum


# user_number = true_number()
# digits_sum = sum_of_digits(user_number)
# print(digits_sum)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал
# каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза
# больше журавликов, чем Петя и Сережа вместе?

# s = int(input('Введите общее количество журавликов: '))
# kate = int(s*2/3)
# serg = int((s*1/6))
# petr = int((s*1/6))
# print(petr, kate, serg)

# Задача 6: Программа, которая проверяет счастливость билета


# def ticket_number():
#     num = int(input('Введите номер билета: '))
#     while num < 100000 or num > 999999:
#         num = int(input('Вы ввели не номер билета, попробуйте еще раз: '))
#     else:
#         return num


# def lucky_ticket(number):
#     sum1 = 0
#     sum2 = 0
#     left_part = number//1000
#     right_part = number % 1000
#     while left_part > 9:
#         sum1 += left_part % 10
#         left_part //= 10
#     while right_part > 9:
#         sum2 += right_part % 10
#         right_part //= 10
#     sum1 += left_part
#     sum2 += right_part
#     if sum1 == sum2:
#         print('Билет счастливый')
#     else:
#         print('Билет не счастливый')


# ticket = ticket_number()
# lucky_ticket(ticket)

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).


def broken_choco():
    n = int(input('Введите n: '))
    m = int(input('Введите m: '))
    k = int(input('Введите k: '))
    if (n > 0 and m > 0 and k > 0):
        i = 1
        j = 1
        possible = False
        while i <= m:
            if i*n == k:
                possible = True
                break
            i += 1
        while j <= n:
            if j*m == k:
                possible = True
                break
            j += 1
        if possible == False:
            print('Столько долек отломить нельзя')
        else:
            print('Столько долек отломить можно')
    else:
        print('Вы ввели один или более размеров равными'
              ' или меньше нуля, попробуйте еще раз')


broken_choco()
