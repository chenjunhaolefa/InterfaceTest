# coding:utf-8
import sys
sys.path.append("..")
from util.operation_excel import OpenationExcel
import data_config

class GetData:
	
	def __init__(self):
		self.operation_excel = OpenationExcel()

	#去获取excel行数，就是我们的case个数	
	def get_case_lines(self):
		return self.operation_excel.get_lines()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(data_config.get_run())
		run_model = self.operation_excel.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#获取是否有header
	def is_header(self,row):
		col = int(data_config.get_header())
		header = self.operation_excel.get_cell_value(row,col)
		# if header == 'yes':
		# 	return data_config.get_header_value()
		# else:
		# 	return None
		return header

	#获取请求数据
	def get_request_method(self,row):
		col = int(data_config.get_request_way())
		request_method = self.operation_excel.get_cell_value(row,col)
		return request_method

	#获取url
	def get_request_url(self,row):
		col = int(data_config.get_url())
		url = self.operation_excel.get_cell_value(row,col)
		return url

	#获取请求数据
	def get_data(self,row):
		col = int(data_config.get_request_data())
		data = self.operation_excel.get_cell_value(row,col)
		if data == '':
			return None
		return data

	#获取预期结果
	def get_expect_data(self,row):
		col = int(data_config.get_expect())
		expect = self.operation_excel.get_cell_value(row,col)
		if expect == '':
			return None
		return expect

	#获取接口名称
	def get_name(self,row):
		col = int(data_config.get_name())
		name = self.operation_excel.get_cell_value(row,col)
		if name == '':
			return None
		return name

	def write_result(self,row,value):
		col = int(data_config.get_result())
		self.operation_excel.write_value(row,col,value)