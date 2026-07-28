#lab9
import pandas as pd
import numpy as np

university = pd.DataFrame ({
    "student_id":[101,102,103,104,105,106,107,108,109,110],
    "name":["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
    "departmenet":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
    "gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
    "scholarship":[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
})

#challenge1 row with highest number of missing values
print(university.loc[university.isnull().sum(axis=1).idxmax()])

#challenge2 replace all missing text fields with not available
for col in university.select_dtypes(include="object").columns:
    university[col] = university[col].fillna("Not Available")
print(university)

#challenge3 replace all missing numerical values using median
for col in university.select_dtypes(include=np.number).columns:
    university[col] = university[col].fillna(
        university[col].median()
    )
print(university)


#challenge4 print only students from cs department
print(
    university[
        university["departmenet"] == "CS"
    ]
)

#challenge5 print students who qualify for scholarship renewal condition gpa >=3.5
for index, row in university.iterrows():
    if row["gpa"] >= 3.5:
        print(row["name"])


#challenge6 create new column called status
#rules:
#gpa >=3.7 Excellent
#gpa >=3.0 Good
#gpa <3.0 At Risk

status = []

for index, row in university.iterrows():

    if row["gpa"] >= 3.7:
        status.append("Excellent")

    elif row["gpa"] >= 3.0:
        status.append("Good")

    else:
        status.append("At Risk")

university["status"] = status

print(university)

#challenge7 count how many students belong to each status category
counts = {}
for index, row in university.iterrows():
    s = row["status"]
    counts[s] = counts.get(s,0) + 1
print(counts)

#challenge8 generate department wise student report using iteration
for dept in university["departmenet"].unique():
    print("\nDepartment:", dept)
    for index, row in university.iterrows():
        if row["departmenet"] == dept:
            print(
                row["student_id"],
                row["name"],
                row["gpa"]
            )

#challenge9 calculate the average gpa without using mean()
#use iteration only
total = 0
count = 0
for index, row in university.iterrows():
    total += row["gpa"]
    count += 1
print(total / count)


#challenge10 calculate total scholarship amount without sum()
#use iteration only
total = 0
for index, row in university.iterrows():
    total += row["scholarship"]
print(total)