# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:56:09 2020

@author: zengl
"""
import pandas as pd
import numpy as np
import sys


#########################################################
#####################提前算好主客观权重##################
########################################################

#########################################################
#######################输入部分##########################
########################################################

# 目前输入6项数据进行CBR计算
def input_attribute_value():
    # 输入一般信息
    a = []
    b = []
    # c = []

    print('首先开始输入一般信息 \n请输入建造年份 \n如2020')
    a1 = int(input())
    if a1 <= 1000 or a1 >= 2020:
        print('年份输入有误')
        sys.exit()
    else:
        a.append(a1)
        # 赋值给年份
        pass

    print('请输入建筑类型 用数字代表 \n1：office 2：commercial 3：residential 4：retail 5：public assembly 6：others')
    a2 = int(input())
    if a2 != 1 and a2 != 2 and a2 != 3 and a2 != 4 and a2 != 5 and a2 != 6:
        print('类型输入有误')
        sys.exit()
    else:
        a.append(a2)
        # 赋值给建造类型
        pass

    print('请输入所有者类型 用数字代表 \n1:government 2:for-profit corporation 3:non-profit corporation')
    a3 = int(input())
    if a3 != 1 and a3 != 2 and a3 != 3:
        print('所有者输入有误')
        sys.exit()
    else:
        a.append(a3)
        # 赋值给所有者类型
        pass

    print('请输入建筑面积 取整数（单位：m^2）')
    a4 = int(input())
    if a4 <= 0:
        print('面积输入有误')
        sys.exit()
    else:
        a.append(a4)
        # 赋值给面积
        pass

    # 输入构件信息

    print('现在开始输入构件信息 \n请输入HVAC系统的能耗效率 用数字代表 \n1：极低 2：低 3：中 4：高 5：极高')
    b2 = int(input())
    if b2 != 1 and b2 != 2 and b2 != 3 and b2 != 4 and b2 != 5:
        print('HVAC效率输入有误')
        sys.exit()
    else:
        b.append(b2)
        # 赋值给照明效率
        pass

    print('请输入照明系统的能耗效率 用数字代表 \n1：极低 2：低 3：中 4：高 5：极高')
    b3 = int(input())
    if b3 != 1 and b3 != 2 and b3 != 3 and b3 != 4 and b3 != 5:
        print('HVAC效率输入有误')
        sys.exit()
    else:
        b.append(b3)
        # 赋值给照明效率
        pass

    return a, b

###############################################
########计算和database里每项的局部相似度########
##############################################

# df = pd.read_excel('database.xlsx', index_col=0)  # 读入我们的数据，数据类型为DataFrame
# print('原始数据库', df)
#
# # 进行局部相似度的转换
#
#
# df = convert_grades(df)
# df.to_excel('local.xlsx')  # 输出化后的数据库
#
# ################################################
# ###########计算两个参数和最终的权重##############
# ###############################################
#
#
# ##############################################
# ##########通过权重计算全局相似度，排序##########
# ##############################################
#
# df1 = pd.read_excel('local.xlsx', index_col=0)
#
# Result = df1.copy()
# df1 = np.array(df1)
# weight = np.array(weight)
# Result['全局相似度'] = np.dot(df1, weight)
# Result['排序'] = Result.rank(ascending=False)['全局相似度']
# Result.to_excel("global_rank.xlsx")  # 导出结果到Result
