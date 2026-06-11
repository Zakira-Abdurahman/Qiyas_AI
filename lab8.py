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


