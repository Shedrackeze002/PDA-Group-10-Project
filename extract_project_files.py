import os
from pathlib import Path

folder = Path(r"C:\Users\Ezesh\OneDrive\Desktop\Shedrack\CMU\PDA\Assignments and Tasks\Project EDA")
files = {
    'analytics': folder / 'Analytics I.docx',
    'prelim': folder / 'Preliminary_Questions_Data_Analytics_assign_group_10.pdf',
    'rubric': folder / 'Rubric.pdf',
    'dataset': folder / 'Intentional Homicide Victims by counts and rates p.xls'
}

out = folder

# Try docx
try:
    from docx import Document
    doc = Document(str(files['analytics']))
    text = []
    for p in doc.paragraphs:
        text.append(p.text)
    with open(out / 'analytics.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(text))
    print('Wrote analytics.txt')
except Exception as e:
    print('docx read failed:', e)

# Try PDF reading with PyPDF2
try:
    import PyPDF2
    def pdf_to_text(path):
        txt = []
        with open(path, 'rb') as fh:
            reader = PyPDF2.PdfReader(fh)
            for p in reader.pages:
                try:
                    txt.append(p.extract_text() or '')
                except Exception:
                    txt.append('')
        return '\n'.join(txt)

    prelim_text = pdf_to_text(files['prelim'])
    with open(out / 'preliminary.txt', 'w', encoding='utf-8') as f:
        f.write(prelim_text)
    rubric_text = pdf_to_text(files['rubric'])
    with open(out / 'rubric.txt', 'w', encoding='utf-8') as f:
        f.write(rubric_text)
    print('Wrote preliminary.txt and rubric.txt')
except Exception as e:
    print('pdf read failed:', e)

# Try Excel preview with pandas
try:
    import pandas as pd
    # read first sheet
    df = pd.read_excel(files['dataset'], sheet_name=0)
    preview = df.head(200)
    preview.to_csv(out / 'homicide_preview.csv', index=False)
    # Save a small description
    desc = df.describe(include='all').to_string()
    with open(out / 'homicide_description.txt', 'w', encoding='utf-8') as f:
        f.write('Columns:\n' + ', '.join(df.columns.astype(str)) + '\n\n')
        f.write('Preview (first 5 rows):\n')
        f.write(preview.head(5).to_string())
        f.write('\n\nDescription:\n')
        f.write(desc)
    print('Wrote homicide_preview.csv and homicide_description.txt')
except Exception as e:
    print('excel read failed:', e)

print('Done')
