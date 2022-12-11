# Типы данных и переменные
# int, float, boolean, str, list, None
# value = None
# print(type(value))

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello \n"world"'
# print(s) # вывод строки
# print(a,'-',b,'-',s)
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

# list = ['1','2','3']
# col = ['hello',1,2,4.5,True]
# print(list)
# print(col)

# print('Введите a: ')
# a = float(input())
# print('Введите b: ')
# b = float(input())
# print(a,'+',b,'=', a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# арифметические опреации +,-,*,/,%,//,**
# приоритет операций **,унарный +, унарный -, *,/,//,%,+,-
# скобки меняют приоритет

# a = 1.31231223
# b = 3
# c = round(a*b, 7)
# print(c)

# a = 3
# a *=5
# print(a)

# логические операции
# >,>=,<,<=,==,!=
# not, and, or не путать с &,|,^
# is, is not, in, not in

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for i in 'qwe - rty':
#     print(i)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('ещё', 'ЕЩЁ'))

# for c in text:
#     print(c)

# ran = range(1,6)
# numbers = list(ran)

# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)

# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)

# for e in colors:
#     print(e*2)

# colors.append('gray')
# print(colors == ['red', 'green', 'blue', 'gray'])
# colors.remove('red')
# del colors[0]
# print(colors)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))
