import numpy as np
import pandas as pd

#1 numpy array of 20 numbers and find the mean
# arr = np.array ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
arr =np.arange(1,21)
print(arr)
print(np.mean(arr))

#2 5x5 matrix and find its transpose
#a = np.array([[1,2,3,4,5], [6, 7, 8, 9,10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
a = np.arange(1,26).reshape(5,5)
print(a)
print(a.T)

#3dataframe of 10 students
data = {
    "Students":["Abel", "Semira", "Hana", "Amir", "Munib", "Habu", "Mama", "Baba", "Zak", "Sumeya"]
}
df =pd.DataFrame(data)
print(df)

#4add a cgpa column
df["CGPA"] = [3, 3.4, 2.7,2, 2.6, 3.6, 3.8, 1.89, 4, 3.9]
print(df)

#5 find highest CGPA
highest = df["CGPA"].max()
print(highest)

print(df.loc[df["CGPA"].idxmax()])

# 6 find the lowest CGPA
lowest = df["CGPA"].min()
print(lowest)

print(df.loc[df["CGPA"].idxmin()])

#7display only student names
print(df["Students"])

#8rename a column
df.rename(columns= {"Students": "Name"}, inplace=True)
print(df)

#9 delete a column
df.drop("CGPA" , axis=1, inplace=True)
print(df)

#save the DataFrame to CSV
df.to_csv("students.csv", index=False)
print("file saved successfully")






