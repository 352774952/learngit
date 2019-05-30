# -*- coding:utf-8 -*-
import unittest
import requests
import json
from public import config
from Logs.log import log1
# 2、继承自unittest.TestCase类
# 格式化json输出


def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)


class TestOne(unittest.TestCase):
    # 3、配置环境：进行测试前的初始化工作
    def setUp(self):
        self.url = 'https://tianqiapi.com/api'
        self.params = {
            "city": "北京"
        }

    # 4、定义测试用例，名字以“test”开头

    def test_post(self):
        response = requests.request("post", self.url, params=self.params)
        result = json.loads(response.text)
        js = get_pretty_print(result)
        # print(js)
        id = result['cityid']
        date = result['data'][0]
        # print(date)
        # 5、定义assert断言，判断测试结果
        self.assertEqual(id, '101010100')

    # 6、清理环境
    def tearDown(self):
        print('testCase after')
        pass


if __name__ == '__main__':
    unittest.main()
