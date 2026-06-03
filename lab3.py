# Exercise 1: Advanced Student Performance Analyzer

students = [
  ("Abel", 45),
  ("Sara", 80),
  ("John", 66),
  ("Mahi", 30),
  ("Helen", 90),
  ("Ruth", 55)

]

def calculate_average(student_List):
    """calculate and return the average score"""
    return sum( score[1] for score in student_List) / len(student_List) 
print(calculate_average(students))

def highest_student(student_List):
    """return the student with the highest score"""
    return max(student_List, key=lambda x: x[1] )
print(highest_student(students))

def lowest_student(student_List):
   """return the student with the lowest score"""
   return min(student_List, key=lambda x: x[1] )
print(lowest_student(students))

def passed_students(student_List):
    """return students with score >= 50"""
    return list(filter(lambda x: x[1] >= 50, student_List))
print(passed_students(students))

def faild_students(student_List):
    """return students with score < 50"""
    return list(filter(lambda x: x[1] < 50, student_List))
print(faild_students(students))

def add_bonus_marks(student_List):
    """add 5 bonus marks using map() and return updated list"""
    return list(map(lambda x: (x[0], x[1] + 5), student_List))
print(add_bonus_marks(students))

def sort_students(student_List):
    """sort students by score using lambda"""
    return sorted(student_List, key=lambda x: x[1])
print(sort_students(students))

def sort_students_desc(student_List):
    """sort students by score descending using lambda"""
    return sorted(student_List, key=lambda x: x[1], reverse=True)
print(sort_students_desc(students))

def process_scores(student_List):
    """square scores above 70 and cube scores below 50 using map()"""
    return list(map(lambda x: (x[0], x[1] ** 2) if x[1] > 70 else (x[0], x[1] ** 3 if x[1] < 50 else (x[0], x[1])), student_List))
print(process_scores(students))

def square_even_cube_odd(student_List):
    """square even scores and cube odd scores using map()"""
    return list(map(lambda x: (x[0], x[1] ** 2) if x[1] % 2 == 0 else (x[0], x[1] ** 3), student_List))
print(square_even_cube_odd(students))

def students_above_70(student_List):
    """return students with scores above 70 using filter()"""
    return list(filter(lambda x: x[1] > 70, student_List))
print(students_above_70(students))

def assign_grades(student_List):
    """assign grades based on score using map()"""
    return list(map(lambda x: (x[0], 'A' if x[1] >= 90 else 'B' if x[1] >= 80 else 'C' if x[1] >= 70 else 'D'), student_List))
print(assign_grades(students))


# Exercise 2: Employee Salary Management System

employees = [
    ("John", "Developer", 5000),
    ("Sara", "Manager", 7000),
    ("Mike", "Designer", 4500),
    ("Helen", "Developer", 6500),
    ("David", "Manager", 7200)
]

def highest_paid_employee(employee_list):
    """return highest paid employee"""
    return max(employee_list, key=lambda x: x[2])
print(highest_paid_employee(employees))

def average_salary(employee_list):
    """calculate average salary"""
    return sum(emp[2] for emp in employee_list) / len(employee_list)
print(average_salary(employees))

def above_average_employees(employee_list):
    """return employees earning above average salary"""
    return list(filter(lambda x: x[2] > average_salary(employee_list), employee_list))
print(above_average_employees(employees))

def add_salary_bonus(employee_list):
    """add 10% bonus salary using map()"""
    return list(map(lambda x: (x[0], x[1], x[2] * 1.1), employee_list))
print(add_salary_bonus(employees))

def sort_by_salary_descending(employee_list):
    """sort employees by salary descending"""
    return sorted(employee_list, key=lambda x: x[2], reverse=True)
print(sort_by_salary_descending(employees))

def double_low_salaries(employee_list):
    """create a list with doubled salaries for salaries below 6000"""
    return list(map(lambda x: (x[0], x[1], x[2] * 2) if x[2] < 6000 else x, employee_list))
print(double_low_salaries(employees))

def developers_only(employee_list):
    """use filter() to return only developers"""
    return list(filter(lambda x: x[1] == "Developer", employee_list))
print(developers_only(employees))

# Exercise 3: Product Inventory Analyzer

products = [
    ("Laptop", 15, 70000),
    ("Mouse", 50, 1200),
    ("Keyboard",30, 2500),
    ("Monitor", 20, 8000),
    ("USB", 100, 500)
    ]

def total_inventory_value(product_List):
    """calculate total inventory value (quantity * price)"""
    return sum(qty * price for product, qty, price in product_List)





