# coding=utf-8
import requests
import json


class RunMain:

    # 构造函数,每次类创建时就初始化，在使用下面测试函数时打开
    def __init__(self, url, headers, method, data=None):
        self.res = self.run_main1(url, headers, method, data)

    def send_get(self, url, data, headers):
        res = requests.get(url=url, data=data, headers=headers).json()
        #return json.dumps(res, indent=2, sort_keys=True)  #这样写返回的是str
        return res

    def send_post(self, url, data, headers):
        res = requests.post(url=url, data=json.dumps(data), headers=headers).json()
        #return json.dumps(res, indent=2, sort_keys=True) #这样写返回的是str
        return res

    def run_main1(self, url, headers, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data, headers)
        else:
            res = self.send_post(url, data, headers)
        return res


# python 测试函数
if __name__ == '__main__':
    url = 'http://learnta.cn/auth/user/loginOrgStudent'
    # url = 'https://learnta.learnta.cn/__api/7/classroom/byTeacherId/3872'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer 51cbd981-f540-3e05-aeaf-2c232c1950c4'}
    data = {"username": "13681881027", "password": "chenjun123", "systemId": 4, "orgId": 1}

    run = RunMain(url, headers, 'POST', data)
    # run = RunMain(url, headers, 'GET')
    print type(data)
    
    print type(headers)
    print run.res





