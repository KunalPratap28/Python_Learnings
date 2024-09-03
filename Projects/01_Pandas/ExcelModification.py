import pandas as pd

df=pd.read_excel('excel1.xlsx',engine='openpyxl')
columns_to_clean=['Age','Id']

def clean_numeric(column):
    df[column]=df[column].astype(str).str.extract(r'(\d+)')
    df[column] = pd.to_numeric(df[column], errors='coerce')

for col in columns_to_clean:
    clean_numeric(col)
    
df.to_excel('cleaned_excel.xlsx',index=False)

print("Columns cleaned")