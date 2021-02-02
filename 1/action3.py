# Action3: 对汽车质量数据进行统计
import pandas as pd

df = pd.read_csv('../car_data_analyze/car_complain.csv')
df = df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))
df['brand'] = df['brand'].apply(lambda x: x.replace('-', ''))
result = df.groupby(['brand'])['id'].agg(['count'])
tags = df.columns[7:]
result2 = df.groupby(['brand'])[tags].agg(['sum'])
result2 = result.merge(result2, left_index=True, right_index=True, how='left')
print(result2)
