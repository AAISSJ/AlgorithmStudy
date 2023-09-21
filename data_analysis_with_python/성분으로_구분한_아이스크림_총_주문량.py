import pandas as pd

# https://school.programmers.co.kr/learn/courses/30/lessons/133026

df1=pd.read_csv('./data/data4.csv')
df2=pd.read_csv('./data/data5.csv')

new_df = df1.join(df2.set_index('FLAVOR'),on='FLAVOR', how='left')
new_df.groupby(['INGREDIENT_TYPE'])['TOTAL_ORDER'].sum().reset_index().sort_values(by='TOTAL_ORDER')

