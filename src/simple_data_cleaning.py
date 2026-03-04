import pandas as pd
import numpy as np

train = pd.read_csv('../data/train.csv')
df = train.copy()

# # 进行对于异常值的统计
# print(df.isnull().sum())
# #
# #
# # 查看Embarked这项所有选项，并总和所有信息
# print(df['Embarked'].value_counts())

df['Embarked'].fillna('S',inplace = True)


