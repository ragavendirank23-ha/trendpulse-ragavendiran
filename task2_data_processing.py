import pandas as pd

df = pd.read_csv("raw_data.csv")

# Clean stars (remove commas, convert to int)
df["stars"] = df["stars"].str.replace(",", "")
df["stars"] = pd.to_numeric(df["stars"], errors="coerce")

# Drop missing values
df.dropna(inplace=True)

# Add derived column
df["name_length"] = df["name"].apply(len)

df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned and saved to cleaned_data.csv")