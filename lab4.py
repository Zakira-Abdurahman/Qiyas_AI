import numpy as np

#exercise 1
print("Numpy imported successfully")

#exercise 2
arr = np.array([1, 2, 3, 4, 5])
print(arr*2)

#exercise 3
grades = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
])
print(grades)

#exercise 4
attendance = np.zeros((5, 7))
print(attendance)

attendance = np.ones((2, 3))
print(attendance)

employee_ids = np.arange(1000, 1010)
print(employee_ids)

time = np.linspace(0, 24, 6)
print(time)

#exercise 5
sales = np.array([
    [100, 150, 200],
    [120, 180, 220],
    [130, 160, 210]
])

print(sales.shape)
print(sales.size)
print(sales.ndim)
print(sales.dtype)

age = np.linspace(1, 25, 5)
print("Age array:", age)
print("Shape:", age.shape)
print("size:", age.size)
print("ndim:", age.ndim)
print("dtype:", age.dtype)

sales = np.array([
    [200, 250, 300],
    [220, 280, 320],    
    [230, 260, 310]
])

print(sales[0, 1])  # Output: 250
print(sales[:, 0])  # Output: [[200], [220], [230]]
print(sales[1, :])  # Output: [220, 280, 320]
print(sales[1, 1])  # Output: 280
print(sales[0])     # Output: [200, 250, 300]
print(sales[0:])    # Output: [[200, 250, 300], [220, 280, 320], [230, 260, 310]]
print(sales[0:2])   # Output: [[200, 250, 300], [220, 280, 320]]
print(sales[0:5])   # Output: [[200, 250, 300], [220, 280, 320], [230, 260, 310]]
print(sales[1:3])   # Output: [[220, 280, 320], [230, 260, 310]]
print(sales[:2])   # Output: [[200, 250, 300], [220, 280, 320]]
print(sales[:,1:])  # Output: [[250], [280], [260]]

sales = np.array([
    [120, 150, 200],
    [130, 160, 210],
    [140, 170, 220]
])

print("tuesday afternoon sales:", sales[1:2, 1])  # Output: [[160]]
print("All morning sales:", sales[:, 0])  # Output: [120, 130, 140]
print("All evening sales:", sales[:, 1])  # Output: [150, 160, 170]
print("monday sales:", sales[0])  # Output: [120, 150, 200]
print("tuesday and wednesday sales:", sales[1:3])  # Output: [[130, 160, 210], [140, 170, 220]]
print("afternoon and evening sales:", sales[:, 1:3])  # Output: [[150, 200], [160, 210], [170, 220]]


#            Math  Physics  Chemistry
# John        80      75       90
# Sarah       65      70       60
# Mike        95      88       92
# Student4    72      78       85

scores = np.array([
    [80, 75, 90],
    [65, 70, 60],
    [95, 88, 92],
    [72, 78, 85]
])

print("sarah's pysics score:", scores[1,1])  # Output: 70
print("All math scores:", scores[:,0])  # Output: [80, 65, 95, 72]
print("all chemistry scores:", scores[:,2])  # Output: [90, 60, 92, 85]
print("john's scores:", scores[0])  # Output: [80, 75, 90]
print("sarah and mike's scores:", scores[1:3])  # Output: [[65, 70, 60], [95, 88, 92]]
print("physics and chemistry scores:", scores[:, 1:3])  # Output: [[75, 90], [70, 60], [88, 92], [78, 85]]
print("the first two students' scores:", scores[:2])  # Output: [[80, 75, 90], [65, 70, 60]]

#homework
print("max score:", np.max(scores))
print("min score:", np.min(scores))
print("mean score:", np.mean(scores))
print("median score:", np.median(scores))
print("average score john:", np.mean(scores[0]))
print("average score sarah:", np.mean(scores[1]))
print("average score mike:", np.mean(scores[2]))
print("average score student4:", np.mean(scores[3]))
print("average score for each student:", np.mean(scores, axis=1))
print("average score for physics:", np.mean(scores[:, 1]))
print("average score for chemistry:", np.mean(scores[:, 2]))
print("average score for math:", np.mean(scores[:, 0]))
print("average score for each subject:", np.mean(scores, axis=0))
print("students with math score above 80:", scores[scores[:, 0] > 80])
