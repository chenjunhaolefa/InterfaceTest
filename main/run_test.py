#coding:utf-8
import sys
sys.path.append("..")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.send_email import SendEmail

class RunTest:

	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommonUtil()
		self.send_mai = SendEmail()

	#程序执行的
	def go_on_run(self):

		pass_count = []
		fail_count = []
		rows_count = self.data.get_case_lines()
		#遍历case按行和列取
		for i in range(1,rows_count):
			url = self.data.get_request_url(i)
			method = self.data.get_request_method(i)
			is_run = self.data.get_is_run(i)
			data = self.data.get_data(i)
			expect = self.data.get_expect_data(i)
			header = self.data.is_header(i)
			name = self.data.get_name(i)
			# print name,'接口测试结果为：'
			if is_run:
				res = self.run_method.run_main(method,url,header,data)
				if self.com_util.is_contain(expect, res):
					self.data.write_result(i,'pass')
					pass_count.append(i)
					# print "测试通过"
					# print type(expect)
					# print type(res)
					# print res
				else:
					self.data.write_result(i,res)
					fail_count.append(i)
					# print "测试失败"
					# print type(res)
					# print res	
		print len(pass_count)
		print len(fail_count)
		self.send_mai.send_main(pass_count,fail_count)

		
if __name__ == '__main__': 
	run = RunTest()
	print run.go_on_run()