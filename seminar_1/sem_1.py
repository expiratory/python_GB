# n = 700
# m = 750
# # days = m//n + int(m%n>0)
# days = (m+n-1)//n
# print(days)

# first_class = 20
# second_class = 21
# third_class = 22
# sum = first_class+second_class+third_class
# # desks = sum//2 + int(sum%2>0)
# desks = (sum+2-1)//2
# print(desks)

# i = 3
# j = 4
# if i == j:
#     print('недостаточно данных')
# else:
#     vagons = j + i - 1
# print(vagons)

year = int(input('Введите год: '))
if (year%400==0 or (year%4==0 and  year%100!=0)):
    print('Год високосный')
else:
    print('Год не високосный')