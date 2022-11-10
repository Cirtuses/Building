import pandas as pd
import numpy as np
import os

RI = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49, 11: 1.51}
dict1 = {'Front the loadbearing concrete and insulation layer': 10, 'Front the loadbearing substrate': 9,
         'Front the built building coating': 8, 'Integrated in windows': 6, 'On the roof': 4,
         'Independent setting': 2, 'Metal tube': 10,
         'Metal panel': 9, 'PCM_ma': 5, 'Multiple Panels': 10, 'Tubes': 9, 'Mansard profile': 8, 'Sphere': 5,
         'Yes_air': 10, 'No_air': 8, 'No_co': 10, 'Insulation material': 8, 'Glass': 7, 'Opaque': 6,
         'Absorbing coloured coating transparent glass': 4, 'Tank': 2, 'Façade/Roof': 10, 'Façade': 9, 'Roof': 7,
         'Equipment': 5, 'Water/air': 10, 'Air': 9, 'PCM_me': 5, 'PVT integrated on facing metal panel': 10,
         'PV integrated on facing metal panel': 9, 'No_in': 7}  # AHP打分字典


def convert_to_number(score):
    return dict1.get(score)


def convert_grades(df):  # 量化数据库，传入Dataframe数据类型
    return df.applymap(convert_to_number)


def ahp(data):
    data = np.array(data)
    # process_data(data)
    print(data)
    m = len(data)
    data = data.astype(float)
    # 计算特征向量
    weight = (data / data.sum(axis=0)).sum(axis=1) / m

    # 计算特征值
    Lambda = sum((weight * data).sum(axis=1) / (m * weight))

    # 判断一致性
    CI = (Lambda - m) / (m - 1)
    if RI[m] == 0:
        CR = 0
    else:
        CR = CI / RI[m]

    if CR < 0.1 or RI[m] == 0:
        print(f'最大特征值：lambda = {Lambda}')
        print(f'特征向量：weight = {weight}')
        print(f'\nCI = {round(CI, 2)}, RI = {RI[m]} \nCR = CI/RI = {round(CR, 2)} < 0.1，通过一致性检验')
        return weight
    else:
        print(f'最大特征值：lambda = {Lambda}')
        print(f'特征向量：weight = {weight}')
        print(f'\nCI = {round(CI, 2)}, RI = {RI[m]} \nCR = CI/RI = {round(CR, 2)} >= 0.1，不满足一致性')

    return weight


def print_result(weight, data):
    Result = data.copy()
    data = np.array(data)
    weight = np.array(weight)
    Result['综合得分指数'] = np.dot(data, weight)
    Result['排序'] = Result.rank(ascending=False)['综合得分指数']
    Result.to_excel("AHP＿Result.xlsx")  # 导出结果到Result
    return Result


def main():
    df = pd.read_excel('input.xlsx', index_col=0)  # 读入我们的数据，数据类型为DataFrame
    print('原始数据库', df)
    print('量化后的数据库', convert_grades(df))
    df = convert_grades(df)
    df.to_excel('score.xlsx')  # 输出化后的数据库

    df1 = pd.read_excel('MainMatrix.xlsx', index_col=0)  # AHP的判断矩阵，数据类型为DataFrame
    df1.to_excel('Matrix.xlsx')  # 分数格式改成小数格式
    print(df1)  # 打印AHP判断矩阵
    weight = ahp(df1)
    print(weight)
    out = print_result(weight, df)
    print(out)  # 输出结果


if __name__ == "__main__":
    main()
