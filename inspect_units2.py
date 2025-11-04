import pandas as pd
from pathlib import Path

p = Path(r"C:\Users\Ezesh\OneDrive\Desktop\Shedrack\CMU\PDA\Assignments and Tasks\Project EDA\homicide_preview.csv")
# read a sample without header and fix
raw = pd.read_csv(p, header=None, nrows=500)
cols = list(raw.iloc[1].fillna('').astype(str))
df = raw.iloc[2:].copy()
df.columns = cols
# drop blank-name columns
df = df.loc[:, [c for c in df.columns if c.strip()!='']]
print('Columns:', list(df.columns))
if 'Unit of measurement' in df.columns:
    units = df['Unit of measurement'].dropna().unique()
    print('\nUnique Units of measurement (sample):', units[:50])
else:
    print('\nUnit of measurement column not found; available columns:')
    print(df.columns.tolist())
if 'Year' in df.columns:
    yrs = pd.to_numeric(df['Year'], errors='coerce')
    print('\nMost recent year in dataset:', int(yrs.max()))
else:
    print('\nYear column not found')
print('\nDone')
