# def split_and_count():
#     first_str = 'a a a b c a a d c d d'
#     data = {}
#     res = ''
#     array = first_str.split()
#     for item in array:
#         if item in data:
#             data[item] += 1
#             res += item + '_' + str(data[item]) + ' '
#         else:
#             data[item] = 0
#             res += item + ' '
#     print(res)

# split_and_count()
    
# n = int(input('Введите N: '))
# if n != 0:
#     max = n
#     while n != 0:
#         n = int(input('Введите N: '))
#         if n > max:
#             max = n
#         else: continue
#     print(max)
# else: print('Чисел нет')

text = 'раз два три четыре пять шесть семь восемь девять раз два три четыре пять шесть семь восемь девять десять'
dict = {}
array = text.split()
res = 0
for item in array:
    if item in dict:
        continue
    else:
        dict[item] = 1
        res += 1
print(res)
