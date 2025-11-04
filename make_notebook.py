import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from pathlib import Path

nb = new_notebook()

nb.cells = [
    new_markdown_cell('# EDA: Intentional Homicide Victims (Group 10)\n\nNotebook generated automatically. Run cells to reproduce the analysis.'),
    new_code_cell("""import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

out_dir = Path('..') / 'outputs'
clean = out_dir / 'homicide_clean.csv'
df = pd.read_csv(clean)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['VALUE'] = pd.to_numeric(df['VALUE'], errors='coerce')
print('Loaded', len(df), 'rows')

df.head()
"""),
    new_markdown_cell('## Top 10 countries in most recent year'),
    new_code_cell("""latest = int(df['Year'].max())
recent = df[df['Year']==latest]
top10 = recent.groupby('Country', as_index=False)['VALUE'].sum().sort_values('VALUE', ascending=False).head(10)
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
import seaborn as sns
sns.barplot(data=top10, x='VALUE', y='Country')
plt.title(f'Top 10 countries by homicide counts ({latest})')
plt.show()
"""),
    new_markdown_cell('## Regional totals'),
    new_code_cell("""region_tot = recent.groupby('Region', as_index=False)['VALUE'].sum().sort_values('VALUE', ascending=False)
region_tot.head()
"""),
    new_markdown_cell('## Global trend'),
    new_code_cell("""world_trend = df.groupby('Year', as_index=False)['VALUE'].sum().sort_values('Year')
import matplotlib.pyplot as plt
plt.figure(figsize=(8,4))
sns.lineplot(data=world_trend, x='Year', y='VALUE', marker='o')
plt.title('Global homicide counts over time')
plt.show()
"""),
    new_markdown_cell('## Notes and next steps\n- To compute rates per 100,000, provide population data for country-year pairs or allow fetching World Bank population series.\n- Add more plots and labeled narrative cells per the rubric.')
]

nb_path = Path('notebooks')
nb_path.mkdir(exist_ok=True)
file_path = nb_path / 'eda_homicide.ipynb'
with open(file_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
print('Wrote', file_path)
