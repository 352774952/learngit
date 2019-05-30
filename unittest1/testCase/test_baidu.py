# -*- coding:utf-8 -*-
# 单个用例执行
# 1、导入模块
import unittest
from Logs.log import log1


# 2、继承自unittest.TestCase类
class TestOne(unittest.TestCase):
    # 3、配置环境：进行测试前的初始化工作
    def setUp(self):
        print('\ncases before')
        pass

    # 4、定义测试用例，名字以“test”开头
    def test_add(self):
        """ test add method """
        print('add...')
        a = 3 + 4
        b = 7
        # 5、定义assert断言，判断测试结果
        self.assertEqual(a, b)
        log1.info("测试通过")

    def test_sub(self):
        """test sub method"""
        print('sub...')
        a = 10 - 5
        b = 5
        self.assertEqual(a, b)
        log1.info("测试通过")

    # 6、清理环境
    def tearDown(self):
        print('testCase after')
        pass


# 7、该方法会搜索该模块下所有以test开头的测试用例方法,并自动执行它们
if __name__ == '__main__':
    unittest.main()
