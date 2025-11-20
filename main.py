import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = '.venv\\archive.zip_unzipped\\Gold-Silver-GeopoliticalRisk_HistoricalData.csv'
df = pd.read_csv(filepath)
print(df.head())


# df = df.drop_duplicates()
# df = df.dropna()
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

cat_col = [col for col in df.columns if df[col].dtype == 'object']
num_col = [col for col in df.columns if df[col].dtype != 'object']

print('Categorical columns:', cat_col)
print('Numerical columns:', num_col)    
