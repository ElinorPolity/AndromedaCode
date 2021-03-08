import pandas
import json
from pandas.io.json import json_normalize
# SCRIPT FOR ORGANIZING DATA
with open('C:/projects/Cognata.json') as f:
  json_data= json.load(f)
df = json_normalize(json_data)
df1=pandas.DataFrame.from_dict(df, orient='columns')
df1=df1[df1.Type != 'Anchor']
df1.to_csv('C:/projects/output.csv')




