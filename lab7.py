#NUMLPY AND PANDAS EXERCISES


#SECTION 1: NUMPY DATA TYPES

#exercise1: Integer Array

import numpy as np
arr = np.array([10, 20, 30, 40])
print(arr.dtype)

#exercise2: Float Array
arr = np.array([1.5, 2.5, 3.5])
print(arr.dtype)

#exercise3: String Array
arr = np.array(["Python", "Java", "SQL"])
print(arr.dtype)  #creates max unicode string

#exercise4: Explicit int32
arr = np.array([1, 2, 3, 4], dtype=np.int32)
print(arr.dtype)

#exercise5: explicit foat32
arr = np.array([1, 2, 3, ], dtype=np.float32)
print(arr.dtype)

#exercise6: type coversion
arr = np.array([1, 2, 3])
new_arr = arr.astype(float)
print(new_arr)

#exercise7: memory usage
arr= np.array([1, 2, 3, 4])
print(arr.nbytes)

#exercise8: array shape
arr= np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

#exercise9: array size
arr =np.array([[1, 2, 3], [4, 5, 6]])
print(arr.size)

#section2 numpy mathematical operations
#exercise10: aray addition

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)

#exercise11: aray subtraction
a= np.array([10,20, 30])
b = np.array([2, 5, 10])
print(a-b)

#exercise12: square root 
arr= np.array([4,9, 16,25])
print(np.sqrt(arr))

#exercise13: variance
arr = np.array([10,20,30,40])
print(np.var(arr))

#exercise14: std
arr = np.array([10,20,30,40])
print(np.std(arr))

#exercise15: matrix addition
a = np.array([[1,2],[3,4]])
b = np.array([[5,6], [7,8]])
print(a+b)

#exercise16: matrix transponse
a = np.array([[1,2,3],[4,5,6]])
print(a.T)

#exercise17: matrix multiplication
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.dot(a,b))

#section3: pandas datafrane creation

#exercise18:dataframe from list
import pandas as pd
courses= ["python", "java", "sql"]
df = pd.DataFrame(courses)
print(df)

#exercise19:dataframe from dictionary
data ={"Name":["Abel", "Hana", "Robel"],
       "Age":[20,21,22]}
df = pd.DataFrame(data)
print(df)

#exercsie20:student dataframe
data= {
    "Name":["Abel", "hana", "Robel"],
    "Department":["CS", "IT", "SE"],
}

df = pd.DataFrame(data)
print(df)

#exercise21: employee dataframe
data= {
    "Employee":["John", "Sara", "Mike"],
    "Salary":[50000,60000,55000]
}
df = pd.DataFrame(data)
print(df)

#exercise22: custom index
data ={
    "Name":["Abel","Hana", "Robel"],
    "Department":["CS", "IT", "SE"]
}
df= pd.DataFrame(data,index=["S1","S2","S3"])
print(df)

#section4: rows, columns,loc[] andiloc[]
#exercise23 select one column
print(df["Name"])

#exercise24: seclect multiple columns
print(df[["Name","Department"]])

#exercsie25: add new collumn
df["CGPA"] = [3.5,3.8,3.2]
print(df)

#exercise26: rename column
df.rename(columns=
          {"Department":"Major"}, inplace=True)
print(df)

#exercise27:delete column
df.drop("CGPA", axis=1, inplace=True)
print(df)

#exercise28: using loc[]
df.index = [101, 102,103]
print(df.loc[102])

#exercise29: multiple rows using loc[]
print(df.loc[[101,103]])

#exerciese30: fist row using iloc[]
print(df.iloc[0])

#exercise31:first two rows
print(df.iloc[0:2])

#exercsie32: first row and first column
print(df.iloc[0,0])


#section5:real world data analysis labs

#exercise33:student marks analysis
data= {
    "Name": ["Abel", "Hana", "Robel"],
    "Math":[80,90,70]
}

df = pd.DataFrame(data)
print(df)
print(df["Math"].mean())
print(df["Math"].max())
print(df["Math"].min())

#exercise34: employee salary analysis

data = {
    "Employee": ["A", "B", "C"],
    "Salary":[40000,60000,50000]
}

df = pd.DataFrame(data)
print(df)
print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Salary"].min())

#exercise35: filter salaries above 50000
print(df[df["Salary"] > 50000])

#exercsie36:course enrollment

data = {
    "Course": ["CS", "IT", "DS", "SE"],
    "Students": [120,100,90,80]
}

df = pd.DataFrame(data)
print(df["Students"].sum())


#exercise37: top enrolled course
print(df.loc[df["Students"].idxmax()])

#section6: mini projects

#project1 : student result system

data= {
    "Name": ["Abel", "Hana", "Robel", "Ruth"],
    "Math": [80,95,60,85],
    "Physics": [70,88,75,90],
    "Chemistry": [90,91,70,95]
}

df = pd.DataFrame(data)
print(df)

df["Total"] = (
    df["Math"] + df["Physics"] + df["Chemistry"]
)
df["Average"] = df["Total"] / 3
print(df)

top_student = df.sort_values(
    by="Average",
    ascending=False
)

print(top_student)














