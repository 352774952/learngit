from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import requests
import json
import xlrd
import unittest
from Logs.log import log1


def open_excel(file='test1.xlsx'):  # 打开要解析的excel文件
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)


def excel_table_byindex(file = 'file.xls', colindex = 0, by_index = 0):#按表的索引读取
    data = open_excel(file)#打开excel文件
    tab = data.sheets()[by_index]#选择excel里面的Sheet
    nrows = tab.nrows#行数
    ncols = tab.ncols#列数
    colName = tab.row_values(colindex)#第0行的值
    list = []#创建一个空列表
    for x in range(1, nrows):      #第一行为标题（第一行为0），所以从第二行开始
        row = tab.row_values(x)
        if row:
            app = {}#创建空字典
            for y in range(0, ncols):
                app[colName[y]] = row[y]
            list.append(app)
    return list


# 格式化json输出

# 4、定义测试用例，名字以“test”开头

path1 = os.path.abspath('..')
path2 = os.path.join(path1, 'Common/test1.xlsx')
listdata = excel_table_byindex(path2)
print(listdata)
for i in range(0, len(listdata)):

    a = listdata[i]['city']
    print(a)

    url = 'https://tianqiapi.com/api'
    params = {
        "city": listdata[i]['city']
    }
    # log1.info(listdata[i][city])
    response = requests.request(listdata[i]['fangshi'], url, params=params)
    print(response.text)
    # result = json.loads(response.text)
    # print(js)
    # id = result['cityid']
    # log1.info(id)
    # print(date)
    # 5、定义assert断言，判断测试结果
    # assertEqual(id, '101010100')
