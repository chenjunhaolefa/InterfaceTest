# coding:utf-8

#对于Excel表数据获取进行封装
class global_var: #数字代表excel表中列的顺序
	Id = '0'
	name = '1'
	url = '2'
	run = '3'
	request_way ='4'
	header = '5'
	data_depend = '6'
	request_data = '7'
	expect = '8'
	result = '9'


# 获取caseid
def get_id():
	return global_var.Id

#获取name
def get_name():
	return global_var.name

#获取url
def get_url():
	return global_var.url

#获取是否运行结果
def get_run():
	return global_var.run

#获取请求方式
def get_request_way():
	return global_var.request_way

#获取header
def get_header():
	return global_var.header

#获取数据依赖
def get_data_depend():
	return global_var.data_depend

#获取请求数据
def get_request_data():
	return global_var.request_data

#获取预期结果
def get_expect():
	return global_var.expect

#获取实际结果
def get_result():
	return global_var.result


#获取header
def get_header_value():
	header = {
	'Content-Type': 'application/json',
    'Authorization': 'Bearer 51cbd981-f540-3e05-aeaf-2c232c1950c4'
    }

