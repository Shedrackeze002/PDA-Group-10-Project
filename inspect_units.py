import pandas as pd
from pathlib import Path
p = Path(r"C:\Users\Ezesh\OneDrive\Desktop\Shedrack\CMU\PDA\Assignments and Tasks\Project EDA\homicide_preview.csv")
# read with header=1 because the file has an extra header row
df = pd.read_csv(p, header=1)
print('Columns:', list(df.columns))
print('\nUnique Units of measurement:')
print(df['Unit of measurement'].dropna().unique())
print('\nMost recent year in dataset:', df['Year'].dropna().astype(int).max())
print('\nSample rows where Unit contains "rate" or "per":')
mask = df['Unit of measurement'].str.lower().str.contains('rate|per', na=False)
print(df[mask].head(10))
