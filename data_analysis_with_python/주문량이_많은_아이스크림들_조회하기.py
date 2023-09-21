import pandas as pd

df = pd.read_csv('./data/data7.csv')
df1= pd.read_csv('./data/data8.csv')

pd.concat([df,df1]).groupby('FLAVOR').sum().reset_index().sort_values(by='TOTAL_ORDER',ascending=False).reset_index().loc[:2,'FLAVOR']
