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
 
#part1 working with missing data
 #exercise1 missing values
print(students.isnull())

#exercise2 missing values in each column
print(students.isnull().sum())

#exercise3 total number of missing values 
print(students.isnull().sum().sum())

#exercise4 percentage of missing values for each column
print(students.isnull().sum() / len(students) * 100)

#exercise5 display only columns with missing values
print(students.columns[students.isnull().any()])

#exercise6 dispaly only rows with missing values
print(students[students.isnull().any(axis=1)])

#exercise7 students with gpa missing 
print(students[students["gpa"].isnull()])

#exercise8 students with scholarship missing
print(students[students["scholarship"].isnull()])

#exercise9 replace missing names with unknown
students["name"] = students["name"].fillna("Unknown")
print(students)

#exercise10 replace missing gpa with mean
students["gpa"] = students["gpa"].fillna(
    students["gpa"].mean()
)
print(students)

#exercise11 replace missing gpa with median gpa
students["gpa"] = students["gpa"].fillna(
    students["gpa"].median()
)

#exercise12 replace missing department using most common department
students["department"] = students["department"].fillna(
    students["department"].mode()[0]
)
print(students)

#exercise13 replace missing scholarship with zero
students["scholarship"] = students["scholarship"].fillna(0)
print(students)

#exercise14 remove rows containing missing values
print(students.dropna())

#exercise15 remove columns containing missing values
print(students.dropna(axis=1))

#exercise16 create gpa missing value flag
students["gpa_missing"] = students["gpa"].isnull()
print(students)

#exercise17 scholarship missing flag
students["scholarship_missing"] = students["gpa"].isnull()
print(students)

#exercise18 columns with highest number of missing values
print(students.isnull().sum().idxmax())

#exercise19 columns with lowest missing values
print(students.isnull().sum().idxmin())

#exercise20 calculate dataset completeness percentage 
100 - (
    students.isnull().sum().sum()
    /
    students.size
) * 100
print(students)

#part 2 iterating over rows and columns
#exercise21 print all column names
for col in students.columns:
    print(col)

#exercise22 column name and data type
for col in students.columns:
    print(col,students[col].dtype)

#exercise23 studnets name using iterrows()
for index, row in students.iterrows():
    print(row["name"])

#exercise24 names and gpa
for index,row in students.iterrows():
    print(row["name"],row["gpa"])

#exercise25 students whose gpa above 3.5
for index, row in students.iterrows():
    if row["gpa"] > 3.5:
        print(row["name"])

#exercise26 scholarship recipients
for index, row in students.iterrows():
    if row["scholarship"] > 0:
        print(row["name"])

#exercise27 create gpa catagories using iteration
catagories = []
for index, row in students.iterrows():
    if row["gpa"] > 3.7:
        catagories.append("Excellent")
    elif row["gpa"] >=3.0:
        catagories.append("Good")
    else:
        catagories.append("At Risk")
students["catagory"] = catagories
print(students)

#exercise28 rows using itertuples()
for row in students.itertuples():
    print(row.student_id, row.name)

#exercise29 count students by department using iteration only
counts = {}
for index, row in students.iterrows():
    dept = row["department"]
    counts[dept] = counts.get(dept, 0) + 1
print(counts)

#exercise30 generate student summary report
for index, row in students.iterrows():
    print(f"Student ID: {row['student_id']}")
    print(f"Name:{row['name']}")
    print(f"Department: {row['department']}")
    print(f"GPA:{row['gpa']}")
    print("-" * 30)



