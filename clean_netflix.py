import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df['director'] = df['director'].fillna('Not Available')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df['duration'] = df['duration'].fillna(df['duration'].mode()[0])
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].fillna(pd.to_datetime('2000-01-01'))

# Standardize text
df['type'] = df['type'].str.lower()
df['rating'] = df['rating'].str.upper()

# Rename columns
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Save the cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)
