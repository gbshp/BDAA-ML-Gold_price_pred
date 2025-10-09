import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = '.venv\archive.zip_unzipped\All_Historical_Data_Separately\Geopolitical Risk Index Daily.csv'
df = pd.read_csv(filepath)

print(df.head())    
print(df.shape)
