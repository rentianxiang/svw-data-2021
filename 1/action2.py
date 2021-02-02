# Action2: 统计全班的成绩
import pandas as pd

df = pd.read_csv('grades.csv')
des = df.describe()
df['total'] = df['语文'] + df['数学'] + df['英语']
df.sort_values('total', ascending=False, inplace=True)
df.reset_index(inplace=True, drop=True)
df['rank'] = df.index + 1
result = df[['姓名', 'rank']]
print(result)
