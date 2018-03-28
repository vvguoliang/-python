#!/Users/vvguoliang/PycharmProjects python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/13 上午11:26
# @Author  : vvguoliang
# @Site    : 
# @File    : sleakla.py
# @Software: PyCharm

"""
__title__ = ''
__author__ = 'vvguoliang'
__mtime__ = '2018/2/13'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏ ┓
            ┏┛┻━━━┛ ┻┓
            ┃   ☃   ┃
            ┃ ┳┛  ┗┳ ┃
            ┃    ┻   ┃
            ┗━┓    ┏━┛
              ┃    ┗━━━┓
              ┃ 神兽保佑 ┣┓
              ┃ 永无BUG！┏┛
              ┗┓┓┏━┳┓┏┛┏┛
               ┃┫┫  ┃┫┫
               ┗┻┛  ┗┻┛
"""

# !/usr/bin/python
# -*- coding:UTF-8 -*-
# 导入需要的包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator

from sklearn import datasets, linear_model
from sklearn.linear_model import LogisticRegression

# 读取文件
df = pd.read_table('num1.txt', header=None, sep=',')
# print(df)
# 读取日期
tdate = sorted(df.loc[:, 0])


# 将以列项为数据，将球号码取出，写入到csv文件中，并取50行数据
# Function to red number to csv file
# noinspection PyTypeChecker
def RedToCsv(h_num, num, csv_name):
    h_num = df.loc[:, num:num].values
    h_num = h_num[2230::-1]
    renum2 = pd.DataFrame(h_num)
    renum2.to_csv(csv_name, header=None)
    fp = open(csv_name)
    s = fp.read()
    fp.close()
    a = s.split('\n')
    a.insert(0, 'numid,number')
    s = '\n'.join(a)
    fp = open(csv_name, 'wb')
    fp.write(s.encode(encoding='utf-8'))
    fp.close()


# 调用取号码函数
# create file
RedToCsv('red1', 1, 'rednum1data.csv')
RedToCsv('red2', 2, 'rednum2data.csv')
RedToCsv('red3', 3, 'rednum3data.csv')
RedToCsv('red4', 4, 'rednum4data.csv')
RedToCsv('red5', 5, 'rednum5data.csv')
RedToCsv('red6', 6, 'rednum6data.csv')
RedToCsv('blue1', 7, 'bluenumdata.csv')


# 获取数据，X_parameter为numid数据,Y_parameter为number数据
# Function to get data
def get_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['numid'], data['number']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))
    return X_parameter, Y_parameter


# 训练线性模型
# Function for Fitting our data to Linear model
def linear_model_main(X_parameters, Y_parameters, predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # regr = LogisticRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {'intercept': regr.intercept_, 'coefficient': regr.coef_, 'predicted_value': predict_outcome}
    return predictions


# 获取预测结果函数
def get_predicted_num(inputfile, num, predictvalue):
    X, Y = get_data(inputfile)
    result = linear_model_main(X, Y, predictvalue)
    print("num " + str(num) + " Intercept value ", result['intercept'])
    print("num " + str(num) + " coefficient", result['coefficient'])
    print("num " + str(num) + " Predicted value: ", result['predicted_value'])


# 调用函数分别预测红球、蓝球
get_predicted_num('rednum1data.csv', 1, 33)
get_predicted_num('rednum2data.csv', 2, 33)
get_predicted_num('rednum3data.csv', 3, 33)
get_predicted_num('rednum4data.csv', 4, 33)
get_predicted_num('rednum5data.csv', 5, 33)
get_predicted_num('rednum6data.csv', 6, 33)
get_predicted_num('bluenumdata.csv', 1, 16)

# 获取X,Y数据预测结果
X1, Y1 = get_data('rednum1data.csv')
predictvalue = 51


#
# X2, Y2 = get_data('rednum2data.csv')
# X3, Y3 = get_data('rednum3data.csv')
# X4, Y4 = get_data('rednum4data.csv')
# X5, Y5 = get_data('rednum5data.csv')
# X6, Y6 = get_data('rednum6data.csv')


# result = linear_model_main(X1, Y1, predictvalue)
# print("red num 1 Intercept value ", result['intercept'])
# print("red num 1 coefficient", result['coefficient'])
# print("red num 1 Predicted value: ", result['predicted_value'])


# Function to show the resutls of linear fit model
def show_linear_line(X_parameters, Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # regr = LogisticRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.figure(figsize=(12, 6), dpi=80)
    plt.legend(loc='best')
    plt.scatter(X_parameters, Y_parameters, color='blue')
    plt.plot(X_parameters, regr.predict(X_parameters), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()


# 显示模型图像，如果需要画图，将“获取X,Y数据预测结果”这块注释去掉，“调用函数分别预测红球、蓝球”这块代码注释下
# show_linear_line(X1, Y1)
