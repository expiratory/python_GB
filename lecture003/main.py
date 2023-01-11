# def f(x):
#     return x**2

# g = f
# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# def calc1(x):
#     return x+10

# print(calc1(10))

# def calc2(x):
#     return x*10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)

# def sum(x, y):
#     return x+y

# sum = lambda x, y: x+y

# def mult(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
    # return op(a, b)

# calc(lambda x, y: x+y, 4, 5)

# list = []

# for i in range(1, 101):
    # if(i%2==0):
    # list.append(i)

# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i% 2 == 0]

# print(list)

# list = [1,2,3,5,8,15,23,38]

# def f(x):
#     return x**2

# list2 = [(i, f(i)) for i in list if i%2 == 0]

# print(list2)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# li = [x for x in range(1, 20)]

# li = list(map(lambda x: x+10, li))

# print(li)

# data = list(map(int, '1 2 3 4 55 67'.split()))

# for e in data:
#     print(e)

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))

# print(res)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4,5,9,14,7]
salary = [111,222,333]
data = list(enumerate(users))
print(data)

