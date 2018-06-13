# coding:utf-8
import unittest
from demo import RunMain
import HTMLTestRunner


class TestMethod(unittest.TestCase):
    
    def setUp(self):
        self.run = RunMain()

    def test_01(self):        
        url = 'http://learnta.cn/auth/user/loginOrgStudent'
        headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer 51cbd981-f540-3e05-aeaf-2c232c1950c4'}
        data = {"username": "13681881027", "password": "chenjun123", "systemId": 4, "orgId": 1}
        res = self.run.run_main(url, headers, 'POST', data) 
        self.assertEqual(res['code'], '0', "测试失败")

    #@unittest.skip('test_02')  # 跳过case2
    def test_02(self):
        url = 'http://learnta.cn/auth/user/loginOrgStudent'
        headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer 51cbd981-f540-3e05-aeaf-2c232c1950c4'}
        data = {"username": "13681881027", "password": "chenjun123", "systemId": 4, "orgId": 1}
        res = self.run.run_main(url, headers, 'POST', data) 
        self.assertEqual(res['code'], '0', "测试失败")


if __name__ == '__main__':
    filepath = "../report/htmlreport.html"  # 创建一个测试报告生成的目录
    fp = file(filepath,'wb')   # 创建一个文件流
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='testreport', description='testdesc')
    runner.run(suite)