import time
import hashlib
import requests
import json


class icpApi:
    def __init__(self):
        # 定义常用变量
        self.icp_api_url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/'

        # 定义公共请求头
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Origin': 'https://beian.miit.gov.cn',
            'Referer': 'https://beian.miit.gov.cn/'
        }

    def get_token(self):
        self.headers['Content-Length'] = '64'
        self.headers['Accept'] = '*/*'
        self.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        api_url = self.icp_api_url + 'auth'
        time_stamp = int(time.time() * 1000)
        md5 = hashlib.md5()
        md5.update(('testtest' + str(time_stamp)).encode(encoding='utf-8'))
        auth_key = md5.hexdigest()
        data = 'authKey={0}&timeStamp={1}'.format(auth_key, time_stamp)
        response = requests.post(api_url, data=data, headers=self.headers)

        if response.status_code == 200:
            json_data = json.loads(response.text)
            if json_data['code'] == 200 and json_data['success'] == True:
                return json_data['params']['bussiness'] # 返回token
            elif json_data['msg']:
                exit(str(json_data['code']) + json_data['msg'])
            else:
                exit('token接口有问题')
        else:
            exit('token接口状态' + str(response.status_code))

    def get_icp_info(self, unit_name, token):
        self.headers['Token'] = token
        self.headers['Accept'] = 'application/json, text/plain, */*'
        self.headers['Content-Type'] = 'application/json'
        api_url = self.icp_api_url + 'icpAbbreviateInfo/queryByCondition'
        # unitName: 单位名称或域名或备案号
        data = {"pageNum": "", "pageSize": "", "unitName": unit_name, "serviceType": "1"}
        response = requests.post(api_url, data=str(data).encode('utf-8'), headers=self.headers)

        if response.status_code == 200:
            json_data = json.loads(response.text)
            if json_data['code'] == 200 and json_data['success'] == True:
                return json_data # 返回原始数据
            elif json_data['msg']:
                exit(str(json_data['code']) + json_data['msg'])
            else:
                exit('查询接口有问题')
        else:
            exit('查询接口状态' + str(response.status_code))

    def response_data(self, info_list):
        # 返回感兴趣的数据
        info_list = info_list['params']['list']
        res_data = dict()
        data_len = len(info_list)
        if data_len == 0:
            res_data['code'] = 0
        else:
            res_data['code'] = 1
            res_data['data'] = list()
            res_data['data'].extend([
                {
                    'domain': info['domain'],
                    'contentTypeName': info['contentTypeName'],
                    'mainLicence': info['mainLicence'],
                    'natureName': info['natureName'],
                    'serviceLicence': info['serviceLicence'],
                    'unitName': info['unitName'],
                    'updateRecordTime': info['updateRecordTime']
                } for info in info_list
            ])
        return res_data

    # 下面的方法作为一个简单的接口
    def info(self, unit_name):
        # 获取token-获取原始数据-获取处理后的数据
        return self.response_data(self.get_icp_info(unit_name, self.get_token()))

# if __name__ == '__main__':
#     token = get_token()
#     info = get_icp_info('粤B2-20090059', token)
#     print(response_data(info))
