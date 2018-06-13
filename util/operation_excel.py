#coding:utf-8
import xlrd
from xlutils.copy import copy

class OpenationExcel:

	def __init__(self,file_name=None,sheet_id=None):
		if file_name:
			self.file_name = file_name
			self.sheet_id = sheet_id			
		else:
			self.file_name = '../case/case.xls'
			self.sheet_id = 0
		self.data = self.get_data()

	#  获取sheets 的内容
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables

	#获取单元格的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows

	#获取某一个单元格的内容
	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)

	def write_value(self,row,col,value):
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		sheet_data = write_data.get_sheet(0)
		sheet_data.write(row, col, value)
		write_data.save(self.file_name)

if __name__ == '__main__':
	opers = OpenationExcel()
	print opers.get_cell_value(1,6)
 