#coding=utf-8
import requests
import json

class RunMethod:
    
    # def __init__(self, method, url, data=None, header=None):
    #     self.res = self.run_main(method,url,header,data)
    
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=json.dumps(json.loads(data)), headers=json.loads(header))
        else:
            res = requests.post(url=url, data=json.dumps(data))
        return res.json()
    
    def get_main(self, url, header,data=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=json.loads(header))
        else:
            res = requests.get(url=url, data=data)
        return res.json()

    
    def run_main(self, method, url, header, data=None):
        res = None
        if method == 'POST':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, header, data)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)

# if __name__ == '__main__':

# 	url = 'http://learnta.cn/auth/user/loginOrgStudent'


# 	headers = {'Content-Type': 'application/json','Authorization': 'Bearer 51cbd981-f540-3e05-aeaf-2c232c1950c4'}
# 	data = {"username": "13681881027", "password": "chenjun123", "systemId": 4, "orgId": 1}

#     # run = RunMethod('GET', url, headers)
# 	run = RunMethod('POST',url, data, headers)
# 	print run.res
