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
