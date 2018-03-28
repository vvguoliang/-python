#!/Users/vvguoliang/PycharmProjects python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/12 下午4:36
# @Author  : vvguoliang
# @Site    : 
# @File    : yuce.py
# @Software: PyCharm

"""
__title__ = ''
__author__ = 'vvguoliang'
__mtime__ = '2018/2/12'
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
import os
from bs4 import BeautifulSoup
import requests
import urllib

url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'


# 伪装成浏览器登入，获取网页代码
def getPage(href):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    req = requests.get(href, headers=headers).content
    soup = BeautifulSoup(req, 'lxml')
    return soup


page = 3


def fun(num1, utl, file):
    tr_class = getPage(utl).find_all('tr')
    for num in range(2, len(tr_class) - 1):
        td_class = tr_class[num].find_all('td')
        td_class_mh = str(td_class[0].text).replace('-', '/')
        align_class = str(td_class[1].text)  # 旗号
        td_class_n = td_class_mh.split('/')  # 年份
        # type_num = type_num + 1
        # align_class = td_class_n[0] + ' ' + align_class + ' ' + td_class_mh + ' '
        if num1 == 1:
            align_class = str(num - page) + ' ' + td_class_n[0] + ' ' + align_class + ' ' + td_class_mh + ' '
        else:
            align_class = str((num1 - page) * 20 + (num - page)) + ' ' + td_class_n[
                0] + ' ' + align_class + ' ' + td_class_mh + ' '
        for x in range(0, 7):
            em_class = td_class[2].find_all('em')
            em_class1 = em_class[x].text
            align_class = align_class + str(int(em_class1)) + ' '
        file.write(str(align_class + '\n'))
    print('第%s批完毕' % num1)


def fun1(num1, utl, file):
    tr_class = getPage(utl).find_all('tr')
    for num in range(2, len(tr_class) - 1):
        td_class = tr_class[num].find_all('td')
        td_class_mh = str(td_class[0].text)
        align_class = str(td_class[1].text)  # 旗号
        td_class_n = td_class_mh.split('/')  # 年份
        # align_class = str(num - 1) + '  ' + td_class_n[0] + '  ' + align_class + '  ' + td_class_mh + '  '
        align_class = td_class_mh + ','
        for x in range(0, 7):
            em_class = td_class[2].find_all('em')
            em_class1 = em_class[x].text
            if x == 6:
                align_class = align_class + em_class1
            else:
                align_class = align_class + em_class1 + ','
        file.write(str(align_class + '\n'))
    print('第%s批完毕' % num1)


def funn():
    tr_class = getPage(url).find_all('tr')
    strong_class = tr_class[-1].find('p', class_='pg').find_all('strong')
    return strong_class[0].text


def fun_zong():
    fp = open('num.txt', 'w')
    for num in range(1, int(funn()) + 1):
        href = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(num) + '.html'
        if num == 1:
            fun(num, url, fp)
        else:
            fun(num, href, fp)
    fp.close()


def fun_zong1():
    fp = open('num1.txt', 'w')
    for num in range(1, int(funn()) + 1):
        href = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(num) + '.html'
        if num == 1:
            fun1(num, url, fp)
        else:
            fun1(num, href, fp)
    fp.close()


# tr_class = getPage(url).find_all('tr')
# td_class = tr_class[2].find_all('td')
# align_class = str(td_class[1].text)
# td_class_n = str(td_class[0].text).split('-')
# print(td_class[0].text)
# print(td_class[1].text)
# print(td_class_n[0])
# print(align_class)

fun_zong()
# fun_zong1()
#
# # 获取URL总页数
# def getPageNum(url):
#     num = 0
#     page = getPage(url)
#     strong = page.find('td', colspan='?')
#     # print strong
#     if strong:
#         result = strong.get_text().split('')
#         # print result
#         list_num = re.find_all('[0-9]{1}', result[1])
#         # print list_num
#         for i in range(len(list_num)):
#             num = num * 10 + int(list_num[i])
#         return num
#     else:
#         return 0
#
#
# # 获取每页双色球的信息
# def getText(url):
#     for list_num in range(1, getPageNum(url)):
#         print(list_num)
#         href = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(list_num) + '.html'
#         page = BeautifulSoup(getPage(href), 'lxml')
#         em_list = page.find_all('em')
#         div_list = page.find_all('td', {'align': 'center'})
#
#         # 初始化
#         n = 0
#         fp = open('num.txt', 'w')
#         for div in em_list:
#             emnum1 = div.get_text()
#             text = div.get_text()
#             text = text.encode('utf-8')
#             n = n - 1
#             if n == 7:
#                 text = text + "\n"
#                 n = 0
#             else:
#                 text = text + ','
#             fp.write(str(text))
#         fp.close()


# from sklearn import linear_model
#
#
# # 获取数据， X_parameter 为numid数据，Y_parameter 为number 数据
# # Function to get data
# def get_data(file_name):
#     data = pd.read_csv(file_name)
#     X_parameter = []
#     Y_parameter = []
#     for single_square_feet, single_price_value in zip(data['numid'], data['number']):
#         X_parameter.append([float(single_square_feet)])
#         Y_parameter.append([float(single_price_value)])
#     return X_parameter, Y_parameter
#
#
# # 训练线性模型
# # Function for Fitting our data to Linear model
# def linear_model_main(X_parameter, Y_parameter, predict_value):
#     # Create linear regression object
#     regr = linear_model.LinearRegression()
#     # regr = LinearRegression
#     regr.fit(X_parameter, Y_parameter)
#     predict_outcome = regr.predict(predict_value)
#     predictions = {'intercept': regr.intercept_, 'coef': regr.coef_, 'predict_value': predict_outcome}
#     return predictions
#
#
# # 获取预测结果函数
# def get_predicted_num(inputfile, num):
#     X, Y = get_data(inputfile)
#     predictvalue = 51
#     result = linear_model_main(X, Y, predictvalue)
#     print('num' + str(num) + 'predict value', result['intercept'])
#     print('num' + str(num) + 'coefficient', result['coefficient'])
#     print('num' + str(num) + 'predict_value', result['predict_value'])
#
#
# # 调用函数分别预测红球、篮球
# get_predicted_num('rednum1data.csv', 1)
# get_predicted_num('rednum2data.csv', 2)
# get_predicted_num('rednum3data.csv', 3)
# get_predicted_num('rednum4data.csv', 4)
# get_predicted_num('rednum5data.csv', 5)
# get_predicted_num('rednum6data.csv', 6)
#
# get_predicted_num('bluenumdata.csv', 1)

# def NN_model_train(seif, trainX, trainY, testX, testY, model_save_path):
#
