#data cleanings and wrangling exercise

import pandas as pd
df = pd.DataFrame({
    "student_id": [101,102,103,102,104,101],
    "name": ["Abel", "Sara","John", "Sara","Helen","Abel"],
    "Score":[80,90,75,90,88,80]
})

#exercise1 removing duplicate records
#identify duplicate rows, count duplicate rows,remove duplicates,keep only last occurrence
print(df.duplicated())
print("Duplicate Count:", df.duplicated().sum())
df_clean = df.drop_duplicates()
df_last = df.drop_duplicates(keep="last")
print(df_clean)
print(df_last)

#exercise2 duplicate emails
#find duplicate eamils and remove duplicate emails
df = pd.DataFrame({
    "id": [1,2,3,4],
    "email": ["a@gmail.com","b@gmail.com","a@gmail.com","c@gmail.com"]
})

duplicates = df[df.duplicated(subset=["email"])]
print(duplicates)
clean_df = df.drop_duplicates(subset=["email"])
print(clean_df)

#exercise3 standardize city names
#convert to uppercase, lowercase,title case
df = pd.DataFrame({
    "city": ["addis ababa","ADDIS ABABA","Addis Ababa","adDis abAba"]
})

df["upper"] = df["city"].str.upper()
df["lower"] = df["city"].str.lower()
df["title"] = df["city"].str.title()
print(df)

#exercise4 remove extra spaces
df = pd.DataFrame({
    "name":[" Abel","Sara "," John"," Helen"]
})
df["name"] = df["name"].str.strip()
print(df)

#exercise5 standardize dates
#convert to datatime,standardize to yyyy-mm-dd,extract year,extract month
pd = pd.DataFrame({
    "date": [ "2026-01-05", "05/02/2026", "March 10, 2026", "2026.04"]
})

df["date"] = pd.to_datetime(df["date"])
df["formatted"] = df["date"].dt.strftime("%Y-%-%d")
df["Year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
print(df)

