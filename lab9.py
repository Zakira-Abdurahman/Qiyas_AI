# Pandas - Working with Missing Data

import pandas as pd
import numpy as np

# Create DataFrame
students = pd.DataFrame({
    "student_id":[101,102,103,104,105,106,107,108,109,110],
    "name":["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
    "department":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
    "gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
    "scholarship":[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
})

print("\n ORIGINAL DATA")
print(students)

# Exercise 1
print("\n  Missing Values")
print(students.isnull())

# Exercise 2
print("\n  Missing Values Count ")
print(students.isnull().sum())

# Exercise 3
print("\nTotal Missing Values")
print(students.isnull().sum().sum())

# Exercise 4
print("\n Percentage of Missing Values")
print((students.isnull().sum()/len(students))*100)

# Exercise 5
print("\n Columns With Missing Values ")
print(students.columns[students.isnull().any()])

# Exercise 6
print("\n  Rows With At Least One Missing Value ")
print(students[students.isnull().any(axis=1)])

# Exercise 7
print("\n Students With Missing GPA ")
print(students[students["gpa"].isnull()])

# Exercise 8
print("\n Students With Missing Scholarship ")
print(students[students["scholarship"].isnull()])

# Exercise 9
print("\n  Column With Highest Missing Values ")
print(students.isnull().sum().idxmax())

# Exercise 10
print("\n GPA Missing Flag ")
students["gpa_missing"] = students["gpa"].isnull()
print(students[["student_id","gpa","gpa_missing"]])

# Exercise 11
print("\n Scholarship Missing Flag ")
students["scholarship_missing"] = students["scholarship"].isnull()
print(students[["student_id","scholarship","scholarship_missing"]])

# Exercise 12
print("\n Remove Rows With Missing Values ")
print(students.dropna())

# Exercise 13
print("\n  Remove Columns With Missing Values ")
print(students.dropna(axis=1))


# Filling Missing Values

# Exercise 14
print("\n Replace Missing Names ==========")
students["name"] = students["name"].fillna("Unknown")
print(students)

# Exercise 15 (Mean)
print("\nExercise 15: Fill GPA Using Mean ")

students_mean = students.copy()

students_mean["gpa"] = students_mean["gpa"].fillna(
    students_mean["gpa"].mean()
)

print(students_mean)

# Exercise 16 (Median)
print("\nFill GPA Using Median ")

students_median = students.copy()

students_median["gpa"] = students_median["gpa"].fillna(
    students_median["gpa"].median()
)

print(students_median)

# Continue with original DataFrame using mean
students["gpa"] = students["gpa"].fillna(
    students["gpa"].mean()
)

# Exercise 17
print("\nFill Department Using Mode")

students["department"] = students["department"].fillna(
    students["department"].mode()[0]
)

print(students)

# Exercise 18
print("\nReplace Missing Scholarship With 0")

students["scholarship"] = students["scholarship"].fillna(0)

print(students)

print("\nFINAL DATAFRAME ")
print(students)