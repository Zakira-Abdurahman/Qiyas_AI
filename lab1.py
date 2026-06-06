name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the python programming World.")

city = input("Enter your city: ")
print("you live in " + city + ".")

food = input("favorite food: ")
print(food, "is perfect for me!")

age = int(input("Enter age: "))
print(age + age)

x= input("Enter a number: ")
y = input("Enter a number: ")
print(x + y)

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
print(x + y)

x, y = input("Enter two numbers: ").split()
print(x)
print(y)

x, y = input("Enter two numbers: ").split()
print(x,y)

first, last = input("first and last name: ").split()
# print(first, last)

x, y, z = input("Enter three numbers: ").split()
print(x+y+z)

username, password = input("Login: ").split()
print(username)

age = int(input("Enter your age: "))
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")


num = int(input("Enter number: "))
if num > 0:
    print("positive number")
else:
    print("negative number")

mark = int(input("mark: "))
if mark >= 50:
    print("pass")
else:
    print("fail")

n = int(input("number: "))
if n % 2 == 0:
    print("even")
else:
    print("odd")

n = 5
for i in range(1, n):
    print(i)

for i in range(5):
    print(i)

for i in range(2, 7):
    print(i)

for i in range (10, 0, -1):
    print(i)

for i in range(3):
    print("Hello")

for i in range(4):
    print(" " * (4 - i) + "*" * (2*i + 1))

for i in range(5):
    print(" " * (5-i) + "*" * (2*i + 1))

d = {'x':123, 'y':456}
for x in d:
    print("%s %d" % (x, d[x]))

d = {"a":1, "b":2}
for k in d:
    print(k, d[k])

d = {"name":"Zakira", "age": 20}
for k in d:
    print(k, "=", d[k])

d = {"math": 90, "physics":80}
for k in d:
    print(k, "=", d[k])

d = {"x": 10, "y":20}
for k, v in d.items():
    print(k,v)

d = {"apple":3, "bannana":5}
for k in d:
    print("fruit:", k)

set1 = {10, 30, 20}
for i in set1:
    print(i)

s = {1, 2, 3 }
for i in s:
    print(i)

s = {"a", "b", "c"}
for i in s:
    print(i)

s = {10, 20, 30}
for i in s:
    print(i + 1)

words = ["python", "for", "python"]
for i in range(len(words)):
    print(words[i])

li = ["python", "for", "python"]
for index in range(len(li)):
    print(li[index])

for i in range(1,5):
    for j in range(i + 1):
        print(i, end=" ")
    print()


