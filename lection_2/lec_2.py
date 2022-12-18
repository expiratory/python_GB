# with open('file.txt', 'a') as data:
#     data.write('line 1111\n')
#     data.write('line 2222\n')

# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close()



# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string(4))

# def concatenatio(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))  #asdw
# print(concatenatio('a', '1'))  #a1d2
# print(concatenatio(1,2,3,4))  # TypeError: ...

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)

# кортеж/tuple - неизменяемый список

# a = (3, 1, 41, 4)
# print(a)
# print(a[-2])
# a[0] = 12  # TypeError

# for item in a:
#     print(item)

# Словари - неупорядоченные коллекции произвольных
# элементов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }

# for k in dictionary:
#     print(dictionary[k])

# Множества

# colors = {'red', 'green', 'blue'}

# print(colors)
# colors.add('red')
# colors.add('gray')
# colors.remove('red')
# print(colors)
# colors.discard('red')  # Удаляет без ошибки
# print(colors)

# list1 = [1,2,3,4,5,]
# list2 = list1

# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

list1 = [1,2,3,4,5,]

# print(list1)
# print(list1.pop(2))
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
print(list1)
print(list1.insert(2, 11))
print(list1)
print(list1.append(11))
print(list1)

