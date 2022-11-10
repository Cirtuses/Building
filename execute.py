import pandas as pd
import numpy as np
import sys

import CBR
import AHP
import Topsis
import collections

ahp_file_name = 'ahp_judge.xlsx'

def judge_categorical_attributes(data, df):  # 类别型 data为我们的输入，df是读取的案列数据
    x = np.array(df)
    data = data[np.newaxis, :]
    y = np.array(data)
    for i in range(x.shape[0] - 1):  # 想构建n行作比较判断
        data = np.insert(data, data.shape[0], y, axis=0)
    print(data)
    print(x)
    j = (x == data)
    # print(j)
    k = j + 0
    print("类别型的判断结果：\n", k)
    return k


def judge_crisp_attributes(data, df, index_list, k):  # 数值型 data为我们的输入，df是读取的案列数据，k是经过类别型判断后的矩阵
    x = np.array(df)  # 数据库案例
    k = k.astype(float)   # 列切片,取第0和1列
    y = x[:, index_list] # 列切片
#    y = x[::, ::3]  # 切片取第1和第4列
#    s = data[0: 4: 3]  # 切片取第0和第4个输入
    s = data[index_list]
    s = s.astype(float)
    r = y - s
    t = np.maximum(r, -r)
    r = 1 - t / (np.max(y, axis=0) - np.min(y, axis=0))
    cnt = 0
    for i in index_list:
        k[::, i] = r[::, cnt] 
        cnt = cnt + 1
    print("清晰属性的执行结果:\n", k)
    return k


def judge_fuzzy_attributes(data, df, index_list, k):  # 模糊型 data输入的target ，df是读取的案列数据，k是经过数值型判断后的矩阵
    x = np.array(df)  # 数据库案例
    y = x[:, index_list] # 列切片
    s = data[index_list]
    r = y - s
    t = np.maximum(r, -r)
    t = t.astype(float)
    t = np.where(t == 1, 5 / 6, t)
    t = np.where(t == 0, 1, t)
    t = np.where(t > 1, 0, t)  # 三次条件判断完成 模糊赋值
    cnt = 0
    for i in index_list:
        k[::, i] = t[::, cnt] 
        cnt = cnt + 1
    print("最终的目标矩阵：\n", k)
    return k


def calculate_parameter(data, subject_weight, object_weight):  # 输入量化的数值和两个权重,返回a,b
    data = data * data
    w = (subject_weight + object_weight) * object_weight
    m = (w * data).sum()  # 分子
    d = (((subject_weight + object_weight) * (subject_weight + object_weight)) * data).sum()
    a = m / d
    b = 1 - a
    return a, b


def print_result(weight, data, target):  # 导出结果
    df_e = pd.read_excel('database_v2.xlsx', index_col=0)
    Result = df_e.copy()
    
    data = np.array(data)
    weight = np.array(weight)
    data = data.astype(float)
    weight = weight.astype(float)
    # print(weight)
    # print(data)
    n = (target * weight).sum()
    m = np.dot(data, weight)
    r = m / n - 1
    s = 1 - np.maximum(r, -r)
    Result['相似度'] = s
    Result['排序'] = Result.rank(ascending=False)['相似度']
    Result = Result.sort_values(by='排序', ascending=True)
    print("结果: \n", Result)
    print("导入 Case-to-Case_v2_Result.xlsx")
    Result.to_excel("Case-to-Case_v2_Result.xlsx")  # 导出结果到Result
    return Result


# def select_ahp_matrix(importance):
#     bflag = True
#     for key,value in importance.items():
#         if value == 0:
#             bflag = False
#             return key
    
#     if bflag == True:
#         print("Error")
    
def ahp_weight_process(importance, ahp_weight_pre):
    ahp_weight = list(ahp_weight_pre) #从大到小
    ahp_weight.sort(reverse=True)
    print(ahp_weight)
    repeat_index = []
    adjust_weight = []
    importance_value = []

    for key, value in importance.items():    
        importance_value.append(value)
    
    print(importance_value)
    repeat_num = find_twice(importance_value)
    print(repeat_num)
    for key, value in enumerate(importance_value):
        if value == repeat_num[0]:
            repeat_index.append(key)
    print(repeat_index)
    if len(repeat_index) != 0:
        importance_value[repeat_index[0]] = 2 if importance_value[repeat_index[0]] == 3 else 3  
    print(importance_value)
    for value in importance_value:    
        adjust_weight.append(ahp_weight[value])
    print(adjust_weight)
    return adjust_weight


def find_twice(my_list):
    freq = collections.Counter(my_list)
    return [num for num, occ in freq.items() if occ == 2]


def read_database(filename, index):
    return pd.read_excel(filename, index_col = index)
    
def add_to_database(filename, index, case): # case is a dict
    serial = []
    df = read_database(filename, index)
    print(df)
    for val in case.values():
        serial.append(val)
    serial = serial[1:]
    row_name = df.shape[0] + 1  #获取行数
    #obj = 'case' + str(row_name)
    # serial.insert(0, obj)
    obj = case['name']
    # df = pd.DataFrame(columns= serial)
    # 采用.loc的方法进行
    #print(df.loc['case7'])
    # print(row_name)
    # print(serial)
    df.loc[obj]= serial  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
    print("new case is {}".format(serial))
    df.to_excel(filename)
    print("success add to database {}".format(filename))
    # 也可采用诸如df.loc['a'] = ['123',30]的形式

def execute_programme(case, importance): #input_a 和 input_b 为list
    
    crisp_index = []
    fuzzy_index = []
    serial = []
    
    df_db = read_database('database_v2.xlsx', 0)

    for val in case.values():
        serial.append(val)
    serial = serial[2:6] + serial[7:]
    print(serial)
    #serial.pop(0, 1, 6) #remove name, U value, fuzzy
    serial = np.array(serial)

    # ahp_file_name = select_ahp_matrix(importance)
    df_ahp = pd.read_excel(ahp_file_name, index_col=0)  # AHP的判断矩阵，数据类型为DataFrame
    a_weight = AHP.ahp(df_ahp)
    a_weight = ahp_weight_process(importance, a_weight)
    # df_b = pd.read_excel('matrixB.xlsx', index_col=0)  # AHP的判断矩阵，数据类型为DataFrame
    # b_weight = AHP.ahp(df_b)

    # df_t = pd.read_excel('matrix0.xlsx', index_col=0)
    # t_weight = AHP.ahp(df_t)

    # a_weight = t_weight[0] * a_weight
    # b_weight = t_weight[1] * b_weight

    # subject_weight = np.append(a_weight, b_weight)  # AHP求得的主观权重
    subject_weight = np.array(a_weight)
    print("主观权重", type(subject_weight), subject_weight)

    df_e = pd.read_excel('database_v2.xlsx', index_col=0)  # 案例数据库导入
    print(df_e)
    df_convert = df_e.drop(labels= ['U value', 'fuzzy evaluation'], axis=1,inplace=False)  # 需要转化的df 
    df_e = Topsis.convert_grades(df_convert)
    # print("经历了convert后的")
    # print(df_e)

    #df_e.insert(0,'U value',df_db.pop('U value'))

    # print("重新插入")
    print(df_e)
    object_weight = Topsis.calculate_entropyweight(df_e)  # topsis求得客观权重
    print("客观权重", type(object_weight), object_weight)
    
    # df_db = read_database('database_v2.xlsx', 0)
    print("数据库： \n",df_db)

    k = judge_categorical_attributes(serial, df_convert)
    s_data = judge_crisp_attributes(serial, df_convert, crisp_index, k)
    # print(s_data)
    # f_data = judge_fuzzy_attributes(input_a, df, s_data)
    (a, b) = calculate_parameter(s_data, subject_weight, object_weight)
    print("计算得到的参数a和b: ", a, b)

    g_weight = a * subject_weight + b * object_weight
    print("最终权重：", g_weight)
    # print(df_e)
    # print(serial)
#    temp = serial[0]
    serial = pd.DataFrame(serial)
    serial = Topsis.convert_grades(serial)
    serial = np.array(serial)
    # serial[0] = temp
    print(serial)
    print_result(g_weight, df_e, serial)
    return a, b


if __name__ == '__main__':
   execute_programme(sys.argv[1], sys.argv[2])
