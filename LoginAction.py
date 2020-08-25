import requests
import json

urlPt = "https://nec-logincenter-pt.amwaynet.com.cn/api/v6/adaAndPwd"
urlFt1 = "https://logincenter-ft1.amwaynet.com.cn/api/v6/adaAndPwd"
urlFt2 = "https://logincenter-ft2.amwaynet.com.cn/api/v6/adaAndPwd"

headers = {
# 'Authorization':Authorization,
#   'channelId':"amwaynews"
}
postData={
    "channelId": "amwaynews",
    "ada": "363333",
    "password": "966966"
}

res = requests.post(url=urlPt,json=postData,headers=headers)
print(res.text)
print(res.elapsed.total_seconds())

res = requests.post(url=urlFt1,json=postData,headers=headers)
print(res.text)
print(res.elapsed.total_seconds())

res = requests.post(url=urlFt2,json=postData,headers=headers)
print(res.text)
print(res.elapsed.total_seconds())


# appId = "/amwaynews"
# appSecret = "/3f952615-2ce3-4a5a-b756-e9a87feb152df4ba4367-90eb-4554-863f-111111111111"
# url=host+appId+appSecret
# res = requests.get(url)
# print(res.text)
# print(res.elapsed.total_seconds())
# jsonDic = json.loads(res.text)
# accessToken = jsonDic['accessToken']
# Authorization = "Bearer "+accessToken
# print("*" * 50)
#
#
#
# url = "https://nec-logincenter-pt.amwaynet.com.cn/sso/api/v6/userticket"
#

# jsonDic = json.loads(res.text)
# data = jsonDic['data']
# jws = data['jws']
# print("*" * 50)



# url = "https://nec-logincenter-pt.amwaynet.com.cn/member-center/v1/userinfo/query/ada"
# headers = {
# 'jws':jws,
# }
# postData={
#   "ada": "363333"
# }
# res = requests.post(url=url,json=postData,headers=headers)
# print(res.text)
# print(res.elapsed.total_seconds())
# print("*" * 50)