import numpy as np
import pandas as pd

#pandas exercise
#exercise set1: dataframe creation
#exercise1

data = {
    "Name": ["Abel", "Sara", "Hana"],
    "Age": [22, 21, 23]
}

df = pd.DataFrame(data)
print(df)


#exercise2 

Department = ["CS", "IT", "SE", "DS"]

df = pd.DataFrame(Department)
print(df)

#exercise set2: exploring dataframes
#exercise3
students = {
    "Name" : ["Abel", "Sara", "John", "Hana"],
    "Age":[22, 21, 23, 20],
    "GPA":[3.8, 3.5, 3.2, 3.9]
}

df= pd.DataFrame(students)
print(df.shape)
print(df.columns)
print(df.dtypes)

#exercsie4
print(df.head(3))

#exercise5
print(df.tail(2))

#exercise set 3: column selection
#exercsie6
print(df["Name"])

#exercsie7
print(df[["Name", "GPA"]])

#exercsie set4: loc and iloc (rows)
#exercise8
print(df.loc[0])

#exercsie9
print(df.iloc[2])

#exercise10
print(df.loc[1, "GPA"])

#exercise11
print(df.iloc[3,1])

#exerscie12
print(df[df["Age"] > 21])

#exercsie13
print(df[df["GPA"] > 3.5])

#exercsie14
print(df[(df["Age"]> 20) & (df["GPA"]> 3.5)])

#exersiese15
department = {
    "Name": ["Abel", "Sara", "John", "Hana"],
    "Department": ["CS", "IT", "SE", "DS"],
    "GPA":[3.8, 3.5, 3.2, 3.9],
    "Age":[22, 21, 23, 20],
}
df = pd.DataFrame(department)
print(df[(df["Department"] =="CS") | (df["Department"] == "IT")])

#exercise set 6: creating new columns
#exercsie 16
#formula : Percentage = GPA * 25
df["Percentage"] = df["GPA"] * 25
print(df)

#exercsie17
#rule: GPA >= 2.0 PASS ELSE FAIL
df["Pass"] = df["GPA"].apply(
    lambda x: "Pass" if x >=2.0 else "Fail"
)
print(df)

#exerscise set 7 : statistics
#exercsie18
print(df["Age"].mean())

#exercise19
print(df["GPA"].max())

#exercise20
print(df["GPA"].min())

#exercise21
print(df["Age"].sum())

#exercise22
print(df["Name"].count())

#exercise set 8: sorting
#exercsie23
#sort by ascending
print(df.sort_values("GPA"))

#exercise24 sort by gpa descending
print(df.sort_values("GPA", ascending=False))

#exercise set 9: missing data
#exerciese 25

data = {
    "Name": ["Abel", "Sara", "John"],
    "Age": [22, np.nan, 20],
    "GPA":[3.5, 3.2, 3.9]
}
df = pd.DataFrame(data)
print(df)

#exercise26 checking missing values
print(df.isnull())

#exercise27 count missing values
print(df.isnull().sum())

#exercise28 replace missing values with 0
print(df.fillna(0))

#exercise29 replace missing values using mean
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
print(df)

#exercsie30 remove rows containing missing values
print(df.dropna())

#exercise set 10: iteration
#exercise31 print all student names using iterrows()
for index, row in df.iterrows():
    print(row["Name"])

#exercsie32 print all student names using itertuples()
for row in df.itertuples():
    print(row.Name)

#exercise33 create scholarship column
#rules, gpa>=3.7 full, gpa>=3.3 partial, otherwise none

def scholarship(gpa):
    if gpa >=3.7:
        return "Full"
    elif gpa >=3.3:
        return "Partial"
    return "None"
df["scholarship"] = df["GPA"].apply(
    scholarship
)
print(df)

#exercise34
#rules: gpa>=3.7 distinction, gpa>=3 very good, gpa>=2 good, otherwise probation

def classify(gpa):
    if gpa >= 3.7:
        return "Distinction"
    elif gpa >= 3.0:
        return "Very Good"
    return "Probation"
df["Classification"] = df["GPA"].apply(
    classify
)
print(df)




#mini project , student performance analysis
students = {
    "StudentID": [1,2,3,4,5],
    "Name": ["Abel", "Sara", "John", "Hana","Samuel"],
    "Department": ["CS", "IT", "SE", "DS", "CS"],
    "Age": [22,21,23,20,24],
    "GPA": [3.8,3.5,3.2,3.9,3.8]

}
df = pd.DataFrame(students)
print("Average GPA")
print(df["GPA"].mean())

print("\nHighest GPA")
print(df["GPA"].max())

print("\nLowest GPA")
print(df["GPA"].min())


df["Percentage"] = df["GPA"] * 25
df["Classification"] = df["GPA"].apply(
    lambda gpa:
    "Distinction" if gpa >= 3.7
    else "Very Good" if gpa >= 3.0
    else "Good"
)
print(df.sort_values(
    "GPA", ascending=False
))