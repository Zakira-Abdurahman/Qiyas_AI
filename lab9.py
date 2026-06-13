#pandas , working with missing data and iterating over rows and columns

import pandas as pd
import numpy as np

students = pd.DataFrame ({
    "student_id":[101,102,103,104,105,106,107,108,109,110],
    "name":["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
    "departmenet":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
    "gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
    "scholarship":[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
})

students

#exercise1 missing values in dataset
print(students.isnull())

#exercsie2 count missing values in each column
print(students.isnull().sum())

#exercise3 total number of missing in dataset
print(students.isnull().sum().sum())

#exercise4 percentage of missing values for each column
print((students.isnull().sum() / len(students)) * 100)

#exercise5 dispaly only columns that contain missing values
print(students.columns[students.isnull().any()])

#exercise6 rows containing at least one missing value
print(students[students.isnull().any(axis=1)])

#exercise7 students whose gpa is missing
print(students[students["gpa"].isnull()])

#exercsie8 scholarship missing
print(students[students["scholarship"].isnull()])

#exercise9 replace missing names by unknown
students["name"] = students["name"].fillna("Unknown")
print(students["name"])

#exercise10 replace missing gpa using mean gpa
students["gpa"] = students["gpa"].fillna(
    students["gpa"].mean()
)
print(students["gpa"])

#exercsie11 replace gpa using median 
students["gpa"] = students["gpa"].fillna(
    students["gpa"].median()
)
print(students["gpa"])

#exercise12 replace department using common department
students["department"] = students["department"].fillna(
    students["department"].mode()[0]
)
print(students)