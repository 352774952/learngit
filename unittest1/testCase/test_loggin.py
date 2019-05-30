# -*- coding:utf-8 -*-
# 单个用例执行
# 1、导入模块
import unittest
from Logs.log import log1
from selenium import webdriver
from Config import session


# 2、继承自unittest.TestCase类
class TestOne(unittest.TestCase):
    # 3、配置环境：进行测试前的初始化工作
    def setUp(self):
        print('\ncases before')
        pass

    # 4、定义测试用例，名字以“test”开头
    def test_loggin(self):
        """ test add method """
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get('http://192.168.7.221:7003/')
        driver.delete_all_cookies()
        driver.add_cookie(session.session)
        driver.refresh()

    # 6、清理环境
    def tearDown(self):
        print('testCase after')
        pass


# 7、该方法会搜索该模块下所有以test开头的测试用例方法,并自动执行它们
if __name__ == '__main__':
    unittest.main()
