#coding:utf-8
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail:
	"""docstring for SendEmail"""
	global email_host
	global send_user
	global password

	email_host = "smtp.163.com"
	send_user = "chenjunhaolefa@163.com"
	password = "chenjun123"
	
	def send_mail(self,user_list,sub,content):
		#发送人
		user = "chenjun"+"<"+send_user+">"
		#构建邮件发送的部分
		msg = MIMEMultipart()
		msg['Subject'] = sub
		msg['From'] = user
		msg['To'] = ";".join(user_list) #分号分割用户列表
		msg.attach(MIMEText(content,_subtype='plain',_charset='utf-8'))#构建邮件格式
		#构造附件并指定编码格式防止邮件乱码
		part = MIMEText(open('E:\\InterfaceTest\\case\\case.xls','rb').read(),'base64','utf-8')
		part.add_header('Content-Disposition', 'attachment', filename="case.xls")
		msg.attach(part)
		#构建发送服务器
		server = smtplib.SMTP()
		server.connect(email_host)
		server.login(send_user,password)
		server.sendmail(user,user_list,msg.as_string())
		server.close()

	def send_main(self,pass_list,fail_list):
		time_stamp = datetime.datetime.now()
		pass_num = float(len(pass_list))
		fail_num = float(len(fail_list))
		count_num = pass_num + fail_num
		#通过率百分比
		pass_result = "%.2f%%" %(pass_num/count_num*100)
		fail_result = "%.2f%%" %(fail_num/count_num*100)

		user_list = ['chenjun@learnta.com']  
		sub = '自动化接口测试报告'+time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
		content = "此次一共运行接口个数为%s个,通过个数为%s个，失败个数为%s个，通过率为%s，失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result)
		self.send_mail(user_list, sub, content)

if __name__ == '__main__': #测试方法
	send = SendEmail()
	send.send_main([1,2,3],[4])
	print "OK"
