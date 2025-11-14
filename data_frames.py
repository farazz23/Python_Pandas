import pandas as pd


data = {
    "Name": ["Faraaz", "Asad", "Osama", "Fahad", "Samad"],
    "Age": [10, 20, 30, 40, 50],
    "City": ["Muzaffarpur", "Dubai", "Gujrat", "Kota", "Lucknow"],
}

# TODO: creating the dictionary into the dataframe
df = pd.DataFrame(data)
print(df)

df.to_json("output_json.json", index=False)
# df.to_csv("output.csv", index=False)
# df.to_excel("output_excel.xlsc", index=False)


#!Loc -> Pandas use the 'loc' attribute to return one or more specified row(s) :
print(f"The First Row :\n {df.loc[0]}")
print(f"The Second Row :\n {df.loc[1]}")
