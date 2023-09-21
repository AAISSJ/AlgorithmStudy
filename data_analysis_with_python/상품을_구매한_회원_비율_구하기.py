import pandas as pd 
# https://school.programmers.co.kr/learn/courses/30/lessons/131534

def custom_round(x, decimal_places=1):
    multiplier = 10 ** decimal_places
    return math.ceil(x * multiplier) / multiplier

df1 = pd.read_csv('./data/data2.csv')
df2 = pd.read_csv('./data/data3.csv')

join_in_2021 = df1['JOINED'].apply(lambda x: True if 2021 ==datetime.datetime.strptime(x,'%Y-%m-%d').year else False)
total_sum =join_in_2021.sum()

df2.dropna(inplace=True)

new_df = df1[join_in_2021].join(df2.set_index('USER_ID'), on='USER_ID',how='inner')
new_df['YEAR'] = pd.to_datetime(new_df['SALES_DATE']).dt.year
new_df['MONTH'] = pd.to_datetime(new_df['SALES_DATE']).dt.month

# 연, 월별로 그룹화하고 고유한 사용자 수를 계산
grouped = new_df.groupby(['YEAR', 'MONTH'])['USER_ID'].unique().reset_index()
grouped['PUCHASED_USERS'] = grouped['USER_ID'].apply(len)
grouped.drop(columns='USER_ID', inplace=True)

# python의 round() 함수는 반올림을 사사오입 원칙으로, 파이썬에서 round() 함수는 정수 부분이 홀수일 경우 올림, 짝수일 경우 내림하여 계산됨 
grouped['PUCHASED_RATIO'] = grouped['PUCHASED_USERS']/join_in_2021.sum()
grouped['PUCHASED_RATIO'] = grouped['PUCHASED_RATIO'].apply(lambda x :custom_round(x))

print(grouped)
