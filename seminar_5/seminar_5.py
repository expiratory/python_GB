# transformation = lambda x: x

# values = [1, 23, 42]
# transformed_values = list(map(lambda x: x**2, values))

# print(transformed_values)
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# import math

# def find_farthest_orbit(list_of_orbits):
#     max = 0
#     for i in list_of_orbits:
#             if i[0] != i[1]:
#                 S = math.pi*i[0]*i[1]
#                 if S > max:
#                     max = S
#                     max_list = (i[0], i[1])
#     print(max_list)


# def find_farthest_orbit(list_of_orbits):
# 	list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
# 	list_of_areas = [(math.pi * i[0] * i[1]) for i in list_of_elliptical_orbits]
# 	max_area_index = list_of_areas.index(max(list_of_areas))
# 	return list_of_elliptical_orbits[max_area_index]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики,
# и возвращают True, если это так. Если значение характеристики для
# разных объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

def same_by(characteristic, objects):
    res_list = []
    for i in objects:
        if characteristic(i) == False:
            res_list.append(1)
        else: res_list.append(0)
    result = set(res_list)
    if len(result) == 1: print('same')
    else: print('different')

values = [2, 10, 6]
same_by(lambda x: x % 7, values)