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
# 将Embarked项全部填充为S
df['Embarked'].fillna('S',inplace = True)

age_median = df['Age'].median()
df['Age'].fillna(age_median,inplace = True)
# 将船舱信息变为有无，添加了一个新的信息在其中
df['Has_Cabin'] = df['Cabin'].notna().astype(int)

print(df.isnull().sum())

df.to_csv('../data/train_cleaned.csv',index=False)