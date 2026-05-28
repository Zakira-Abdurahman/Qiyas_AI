# def greet():
#     print("Hello, World!")

# greet()

# def add(x, y):
#     print(x + y)
# add(5, 6)

# def myFun(num):
#     if num % 2 == 0:
#         print("square:", num ** 2)
#     else:
#         print("cube:", num ** 3)
# myFun(3)
# myFun(4)

# def check(num):
#     if num > 0:
#         print(f"{num}: Positive")
#     else:
#         print(f"{num}: Negative")
# check(5)
# check(-3)

# def add(a,b):
#     return a + b
# result = add(10, 20)
# print(result)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(0))
# print(factorial(5))

# result = [x for x in range(10)]
# print(result)

# range_value = range(0, 10)
# result = [value for value in range_value if value % 2 == 0]
# print(result)

# nums = [x**2 for x in range(1,6)]
# # print(nums)

# list = [num**3 if num % 2 ==0 else num**2 for num in range(1, 10)]
# print(list)

# mat = [[1,2,3], [4,5,6], [7,8,9]]
# res = [val for row in mat for val in row]
# print(res)

# def square(x):
#     return x * 2
# print(square(2))

# print((lambda x: x * 2)(5))

# func = [lambda arg=x: arg*10 for x in range(1, 7)]
# print(func[0]())
# print(func[1]())        
# print(func[2]())
# print(func[3]())
# print(func[4]())
# print(func[5]())

# def add(*args):
#     print(args)
# add(1,2,3)

# def total(*nums):
#     print(sum(nums))
# total(1,2,3,4,5)

# def person(**kwargs):
#     print(kwargs)
# person(name="Zak", age=20)