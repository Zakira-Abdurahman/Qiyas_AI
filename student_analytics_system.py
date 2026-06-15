# Zakira Abdurahman
import pandas as pd
import numpy as np

university = pd.DataFrame ({
    "student_id":[101,102,103,104,105,106,107,108,109,110],
    "name":["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
    "departmenet":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
    "gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
    "scholarship":[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
})

#data cleaning
#1 count missing values
print(university.isnull().sum().sum())

#2percentage of missing value
print(university.isnull().sum() / len(university) * 100)

#3replace missing names with unknown
university["name"] = university["name"].fillna("Unknown")
print(university["name"])

#4replace missing departments with mode
university["departmenet"] = university["departmenet"].fillna(
    university["departmenet"].mode()[0]
)
print(university["departmenet"])

#5replace missing gpa using median
university["gpa"] = university["gpa"].fillna(
    university["gpa"].median()
)
print(university["gpa"])

#6replace missing scholarship with zero

university["scholarship"] = university["scholarship"].fillna(0)
print(university)

#data analysis
#7 count students by department
print(university["departmenet"].value_counts())

#8 count scholarship recipients
print((university["scholarship"] > 0).sum())

#9 highest gpa
print(university["gpa"].max())

#10 lowest gpa
print(university["gpa"].min())

#11 average gpa
print(university["gpa"].mean())

#12 total scholarship amount
print(university["scholarship"].sum())

#iterative tasks 
#13 generate a report for every student
for index, row in university.iterrows():
     print(f"Student ID : {row['student_id']}")
     print(f"Name: {row['name']}")
     print(f"Department : {row['departmenet']}")
     print(f"GPA: {row['gpa']}")
     print(f"Scholarship: {row['scholarship']}")
     print("-" * 35)


#14 create gpa categories: excellent good at risk
gpa_category = []

for index, row in university.iterrows():
    if row["gpa"] >= 3.7:
        gpa_category.append("Excellent")
    elif row["gpa"] >= 3.0:
        gpa_category.append("Good")
    else:
        gpa_category.append("At Risk")

university["gpa_category"] = gpa_category
print(university)

#15 create scholarship catagories: full scholarship partial no scholarship
scholarship_category = []

for index, row in university.iterrows():

    if row["scholarship"] >= 5000:
        scholarship_category.append("Full Scholarship")

    elif row["scholarship"] > 0:
        scholarship_category.append("Partial Scholarship")

    else:
        scholarship_category.append("No Scholarship")

university["scholarship_category"] = scholarship_category

print(university)

#final report
#create final dataframe containing studnet id , name , department, gpa, gpa category scolarship amount , scholarship catagory 
final_report = university[[
    "student_id",
    "name",
    "departmenet",
    "gpa",
    "gpa_category",
    "scholarship",
    "scholarship_category"
]]

print(final_report)

