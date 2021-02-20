import pandas as pd
import requests





med_path = 'https://api.endlessmedical.com/v1/dx/GetFeatures'

df = pd.read_json(med_path)
print(df)