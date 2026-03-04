import pandas as pd

#加载
train = pd.read_csv('../data/train.csv')
#行列信息
print(train.shape)
#类型和缺失
print(train.info())
#数据的统计，数据中特殊的值
print(train.describe())
