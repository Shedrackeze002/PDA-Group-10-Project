import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

data_xls = Path(r"C:\Users\Ezesh\OneDrive\Desktop\Shedrack\CMU\PDA\Assignments and Tasks\Project EDA\Intentional Homicide Victims by counts and rates p.xls")
preview = Path(r"C:\Users\Ezesh\OneDrive\Desktop\Shedrack\CMU\PDA\Assignments and Tasks\Project EDA\homicide_preview.csv")

p = data_xls
out_dir = Path(r"C:\Users\Ezesh\OneDrive\Desktop\Shedrack\CMU\PDA\Assignments and Tasks\Project EDA\outputs")
out_dir.mkdir(exist_ok=True)

# Read excel (try to locate header row by searching for 'Iso3' column name)
try:
    raw_xl = pd.read_excel(p, sheet_name=0, header=None)
    # find header row index where any cell contains 'Iso3'
    header_row = None
    for idx in range(min(10, len(raw_xl))):
        row_vals = raw_xl.iloc[idx].astype(str).str.lower().values
        if any('iso3' in v or 'iso_3' in v or 'iso3_code' in v for v in row_vals):
            header_row = idx
            break
    if header_row is not None:
        cols = list(raw_xl.iloc[header_row].astype(str))
        df = raw_xl.iloc[header_row+1:].copy()
        df.columns = cols
    else:
        # fallback: try reading with default header
        df = pd.read_excel(p, sheet_name=0)
except Exception:
    # fallback to previously created preview csv
    df = pd.read_csv(preview, skiprows=1)

# Standardize column names
df.columns = [c.strip() for c in df.columns.astype(str)]
# Keep relevant columns and coerce types
cols_needed = ['Iso3_code','Region','Subregion','Country','Source','Dimension','Category','Sex','Age','Year','Unit of measurement','VALUE']
available = [c for c in cols_needed if c in df.columns]
print('Using columns:', available)
sub = df[available].copy()
sub['Year'] = pd.to_numeric(sub['Year'], errors='coerce')
sub['VALUE'] = pd.to_numeric(sub['VALUE'], errors='coerce')
sub = sub.dropna(subset=['Country','Year','VALUE'])

# Save cleaned CSV
clean_csv = out_dir / 'homicide_clean.csv'
sub.to_csv(clean_csv, index=False)
print('Wrote', clean_csv)

# Quick summaries
latest_year = int(sub['Year'].max())
print('Most recent year in cleaned data:', latest_year)
recent = sub[sub['Year']==latest_year]

# Top 10 countries by counts in most recent year
top10 = recent.groupby('Country', as_index=False)['VALUE'].sum().sort_values('VALUE', ascending=False).head(10)
print('\nTop 10 countries by homicide counts in', latest_year)
print(top10)

# Plot top10 bar
plt.figure(figsize=(10,6))
sns.barplot(data=top10, x='VALUE', y='Country', palette='rocket')
plt.title(f'Top 10 countries by homicide counts ({latest_year})')
plt.xlabel('Counts')
plt.tight_layout()
plt.savefig(out_dir / 'top10_countries.png')
plt.close()

# Regional comparison: total counts by Region for recent year
if 'Region' in sub.columns:
    region_tot = recent.groupby('Region', as_index=False)['VALUE'].sum().sort_values('VALUE', ascending=False)
    plt.figure(figsize=(8,5))
    sns.barplot(data=region_tot, x='VALUE', y='Region', palette='mako')
    plt.title(f'Homicide counts by Region ({latest_year})')
    plt.tight_layout()
    plt.savefig(out_dir / 'region_counts.png')
    plt.close()

# Trend over time for world totals (if 'World' present or sum across years)
world_trend = sub.groupby('Year', as_index=False)['VALUE'].sum().sort_values('Year')
plt.figure(figsize=(8,4))
sns.lineplot(data=world_trend, x='Year', y='VALUE', marker='o')
plt.title('Global homicide counts over time (all countries)')
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig(out_dir / 'global_trend.png')
plt.close()

# Sex comparison (Male vs Female) for recent year
if 'Sex' in sub.columns:
    sex_comp = recent.groupby('Sex', as_index=False)['VALUE'].sum()
    plt.figure(figsize=(6,4))
    sns.barplot(data=sex_comp, x='Sex', y='VALUE', palette='pastel')
    plt.title(f'Homicide counts by Sex ({latest_year})')
    plt.tight_layout()
    plt.savefig(out_dir / 'sex_counts.png')
    plt.close()

# Distribution of VALUE (counts) and outliers
plt.figure(figsize=(6,4))
sns.histplot(sub['VALUE'].dropna(), bins=60, log_scale=(False,True))
plt.title('Distribution of homicide counts (log scale for y)')
plt.tight_layout()
plt.savefig(out_dir / 'value_distribution.png')
plt.close()

# Share of top 10 countries each year (concentration) - compute share for latest year
if 'Country' in sub.columns:
    total_latest = recent['VALUE'].sum()
    top10_latest = top10['VALUE'].sum()
    share_top10 = 100 * top10_latest / total_latest if total_latest>0 else 0
else:
    share_top10 = None

# Produce a draft markdown report answering preliminary questions (8 chosen)
report = []
report.append('# Final report draft — Intentional Homicide (group 10)')
report.append(f'**Most recent year analyzed:** {latest_year}\n')
report.append('## Key findings (draft)')
report.append('1. Top countries:')
report.append(top10.to_markdown(index=False))
report.append('\n')
report.append('2. Regional totals (most recent year):')
if 'Region' in sub.columns:
    report.append(region_tot.to_markdown(index=False))
report.append('\n')
report.append('3. Global trend: See outputs/global_trend.png')
report.append('\n')
report.append('4. Share of top 10 countries in latest year:')
report.append(f'{share_top10:.2f}%')
report.append('\n')
report.append('5. Sex differences (counts): See outputs/sex_counts.png')
report.append('\n')
report.append('6. Distribution and outliers: See outputs/value_distribution.png')

report_path = out_dir / 'final_report_draft.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(report))
print('Wrote report draft to', report_path)

print('\nDone. Outputs in', out_dir)
