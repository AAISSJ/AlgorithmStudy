# https://school.programmers.co.kr/learn/courses/30/lessons/157340
import pandas as pd


df = pd.read_csv('./data/data6.csv')
df['START_DATE'] = pd.to_datetime(df['START_DATE'])
df['END_DATE'] = pd.to_datetime(df['END_DATE'])

df['AVAILABILITY'] = df.apply(lambda x: "대여중" if x['START_DATE']<= datetime.datetime.strptime('2022-10-16',"%Y-%m-%d") <=x['END_DATE'] else "대여 가능", axis=1)
result_df = df.groupby('CAR_ID')['AVAILABILITY'].apply(lambda x: '대여중' if '대여중' in x.values else '대여 가능').reset_index()

