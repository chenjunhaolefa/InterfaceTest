# coding:utf-8
import unittest
from demo import RunMain

class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print '类执行之前的方法'

    @classmethod
    def tearDownClass(cls):
        print '类执行之后的方法'

    # 每次方法执行之前
    def setUp(self):
        print 'test-->setup'

    # 每次方法执行之后
    def tearDown(self):
        print 'test-->tearDown'

    def test_01(self):
        print '这是第一个测试方法'

    def test_02(self):
        print '这是第二个测试方法'


if __name__ == '__main__':
        unittest.main()
