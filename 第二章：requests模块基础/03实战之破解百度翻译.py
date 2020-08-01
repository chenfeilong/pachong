import requests
import json
# 1.指定url
post_url = 'https://fanyi.baidu.com/sug'
# 2.UA伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
# 3.post请求参数处理
word = input('关键字:')
data = {
    'kw': word
}

# 4.请求发送
response = requests.post(post_url, data=data, headers=headers)

# 5获取响应数据:json()方法返回的是obj
dic_obj = response.json()
print(dic_obj)

# 持久化存储
fileName = word+'.json'
fp = open(fileName, 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)
print('over!!')