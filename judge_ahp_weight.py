import AHP
import pandas as pd

df_a = pd.read_excel('test.xlsx', index_col=0)  # AHP的判断矩阵，数据类型为DataFrame
# df_a.to_excel('Matrix.xlsx')  # 分数格式改成小数格式
print(df_a)  # 打印AHP判断矩阵
a_weight = AHP.ahp(df_a)