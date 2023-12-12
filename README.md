# G了已经

前端接口：
```js
authKey: function(g, A, I) {
                return y.a.MD5(g + A + I).toString(y.a.enc.Hex)
}
// g = 'test' A = 'test' I = timeStamp
```
## 使用
实时获取icp备案的接口信息
```python
from icpApi import *
icp = icpApi()
print(icp.info('粤B2-20090059'))
```
导入这个类二开web 批量脚本

## get_token
```
{'code': 401, 'msg': '没有通过身份验证', 'success': False}

{'code': 200, 'msg': '操作成功', 'params': {'bussiness': 'eyJ0eXBlIjoxLCJ1IjoiMDk4ZjZiY2Q0NjIxZDM3M2NhZGU0ZTgzMjYyN2I0ZjYiLCJzIjoxNjk3NjA2MzE0MTExLCJlIjoxNjk3NjA2Nzk0MTExfQ.10MhJ6tB7bgHLzs_fP9VJSlIFqPYwnZEenFcfUWjak0', 'expire': 300000, 'refresh': 'eyJ0eXBlIjoyLCJ1IjoiMDk4ZjZiY2Q0NjIxZDM3M2NhZGU0ZTgzMjYyN2I0ZjYiLCJzIjoxNjk3NjA2MzE0MTExLCJlIjoxNjk3NjA3MDk0MTExfQ.9xnoEpxCj-85JM1NYGJNPx-jow7HNyOK5bGlzRxZmCA'}, 'success': True}
```

## get_icp_info
```python
{"success":false,"code":500,"msg":"服务器异常"}

{"success":false,"code":401,"msg":"token过期,请及时刷新页面"}

{"code":200,"msg":"操作成功","params":{"endRow":0,"firstPage":1,"hasNextPage":false,"hasPreviousPage":false,"isFirstPage":true,"isLastPage":true,"lastPage":1,"list":[{"contentTypeName":"宗教、宗教、出版、新闻、出版、出版、新闻、宗教、文化、宗教","domain":"qq.com","domainId":190000203203,"leaderName":"","limitAccess":"否","mainId":547280,"mainLicence":"粤B2-20090059","natureName":"企业","serviceId":4134047,"serviceLicence":"粤B2-20090059-5","unitName":"深圳市腾讯计算机系统有限公司","updateRecordTime":"2023-10-18 10:27:25"}],"navigatePages":8,"navigatepageNums":[1],"nextPage":1,"pageNum":1,"pageSize":10,"pages":1,"prePage":1,"size":1,"startRow":0,"total":1},"success":true}
```


```python
 # res_data['data'].append(dict({'domain': info['domain'],
        #                               'contentTypeName': info['contentTypeName'],
        #                          'mainLicence': info['mainLicence'],
        #                          'natureName': info['natureName'],
        #                          'serviceLicence': info['serviceLicence'],
        #                          'unitName': info['unitName'],
        #                          'updateRecordTime': info['updateRecordTime']
        #                          }) for info in info_list)
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
```