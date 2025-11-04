import pandas as pd
from pathlib import Path
p = Path(r"C:\Users\Ezesh\OneDrive\Desktop\Shedrack\CMU\PDA\Assignments and Tasks\Project EDA\homicide_preview.csv")
# skip first two rows, the third row is the real header
df = pd.read_csv(p, skiprows=2, header=0)
print('Columns:', list(df.columns))
if 'Unit of measurement' in df.columns:
    print('\nUnique Units of measurement (sample):', df['Unit of measurement'].dropna().unique()[:50])
else:
    print('\nUnit of measurement column not found; available columns:')
    print(df.columns.tolist())
if 'Year' in df.columns:
    yrs = pd.to_numeric(df['Year'], errors='coerce')
    print('\nMost recent year in dataset:', int(yrs.max()))
else:
    print('\nYear column not found')
print('\nCounts for Unit of measurement (top 10):')
if 'Unit of measurement' in df.columns:
    print(df['Unit of measurement'].value_counts().head(10))
print('\nDone')
