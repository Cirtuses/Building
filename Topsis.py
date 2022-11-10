import pandas as pd
import numpy as np

dict1 = {'Front the loadbearing concrete and insulation layer': 10, 'Front the loadbearing substrate': 9,
         'Front the built building coating': 8, 'Integrated in windows': 6, 'On the roof': 4,
         'Independent setting': 2, 'Metal tube': 10,
         'Metal panel': 9, 'PCM_ma': 5, 'Multiple Panels': 10, 'Tubes': 9, 'Mansard profile': 8, 'Sphere': 5,
         'Yes_air': 10, 'No_air': 8, 'No_co': 10, 'Insulation material': 8, 'Glass': 7, 'Opaque': 6,
         'Absorbing coloured coating transparent glass': 4, 'Tank': 2, 'Façade/Roof': 10, 'Façade': 9, 'Roof': 7,
         'Equipment': 5, 'Water/air': 10, 'Air': 9, 'PCM_me': 5, 'PVT integrated on facing metal panel': 10,
         'PV integrated on facing metal panel': 9, 'No_in': 7,
         
         'very low':0.3, 'low':0.6, 'medium':0.9, 'high':1.2, 'very high':1.5,
          'ventilation':0.4, 'solar collector':0.6, 'solar power':0.8,  'ventilation; solar collector':1.0,
          'ventilation;solar power':1.2,'ventilation;solar collector;solar power':1.4, 'solar collector;solar power':1.6 }  # AHP打分字典


def convert_to_number(score):
    return dict1.get(score)


def convert_grades(df):  # 量化数据库，传入Dataframe数据类型
    return df.applymap(convert_to_number)


def topsis(data, weight=None):  # topsis算法过程，传入量化后的数据库和权重
    # 归一化
    data = data / np.sqrt((data ** 2).sum())

    # 最优最劣方案
    Z = pd.DataFrame([data.min(), data.max()], index=['负理想解', '正理想解'])

    # 距离
    weight = calculate_entropyweight(data) if weight is None else np.array(weight)
    Result = data.copy()
    print("data.copy():", Result)
    Result['与正理想解接近程度'] = np.sqrt(((data - Z.loc['正理想解']) ** 2 * weight).sum(axis=1))
    Result['与负理想解接近程度'] = np.sqrt(((data - Z.loc['负理想解']) ** 2 * weight).sum(axis=1))

    # 综合得分指数
    Result['综合得分指数'] = Result['与负理想解接近程度'] / (Result['与负理想解接近程度'] + Result['与正理想解接近程度'])
    Result['排序'] = Result.rank(ascending=False)['综合得分指数']

    # Result.to_excel(r"F:\Py1\data\Result.xlsx")
    # Z.to_excel(r"F:\Py1\data\Z.xlsx")
    Result.to_excel("Topsis_v1_Result.xlsx")  # 导出结果到Result
    Z.to_excel("Z_v1.xlsx")  # 导出每一列的正负理想解
    print(type(weight))
    return Result, Z, weight


# 数据处理，由于我们事先做好所以不用这三种数据处理方式
# def dataDirection_1(datas, offset=0):  # 极小型
#     def normalization(data):
#         return 1 / (data + offset)
#
#     return list(map(normalization, datas))
#
#
# def dataDirection_2(datas, x_min, x_max):  # 中间型
#     def normalization(data):
#         if data <= x_min or data >= x_max:
#             return 0
#         elif x_min < data < (x_min + x_max) / 2:
#             return 2 * (data - x_min) / (x_max - x_min)
#         elif x_max > data >= (x_min + x_max) / 2:
#             return 2 * (x_max - data) / (x_max - x_min)
#
#     return list(map(normalization, datas))
#
#
# def dataDirection_3(datas, x_min, x_max, x_minimum, x_maximum):  # 区间型
#     def normalization(data):
#         if x_min <= data <= x_max:
#             return 1
#         elif data <= x_minimum or data >= x_maximum:
#             return 0
#         elif x_max < data < x_maximum:
#             return 1 - (data - x_max) / (x_maximum - x_max)
#         elif x_min > data > x_minimum:
#             return 1 - (x_min - data) / (x_min - x_minimum)
#
#     return list(map(normalization, datas))


def calculate_entropyweight(data):  # 熵值法求权重
    data = np.array(data)
    # 归一化

    P = data / data.sum(axis=0)

    # 计算熵值
    E = np.nansum(-P * np.log(P) / np.log(len(data)), axis=0)

    # 计算权系数
    return (1 - E) / (1 - E).sum()


def main():
    weight = []  # 权重
    out = []  # topsis的输出结果
    print(dict1)  # 输出字典
    df = pd.read_excel('input.xlsx', index_col=0)  # 读入我们的数据，数据类型为DataFrame
    height, width = df.shape
    print(height, width, type(df))  # 打印Dataframe的属性
    print('原始数据库', df)
    print('量化后的数据库', convert_grades(df))
    df = convert_grades(df)
    print(df)
    df.to_excel('score.xlsx')  # 输入量化后的数据库

    weight = calculate_entropyweight(df)
    print('熵值法求得的权重：', weight)
    out = topsis(df, weight)
    print(out)


if __name__ == "__main__":
    main()
