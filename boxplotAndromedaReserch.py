import json
import pandas
from pandas.io.json import json_normalize
import numpy as np
import matplotlib.pyplot as plt
# code for BOXPLOT
with open('C:/projects/Cognata.json') as f:
  json_data= json.load(f)
df = json_normalize(json_data)
df1=pandas.DataFrame.from_dict(df, orient='columns')
df1=df1[df1.Type != 'Anchor']
Brake=df1.Brake
Brake= Brake[np.logical_not(np.isnan(Brake))]
print(Brake)
plt.boxplot(Brake, notch=None, vert=None, patch_artist=None, widths=None)
plt.show()
print(df1.columns)



