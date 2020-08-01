import requests
import json
url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
url2 = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
id_list = []
for page in range(1, 2):

    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': ''
    }
    json_ids = requests.post(url=url, data=data, headers=headers).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])

# print(response.text)
list_c = []
for id in id_list:
    data = {'id':  id}
    # print(data)
    json_obj = requests.post(url=url2, data=data, headers=headers).json()
    list_c.append(json_obj)

print(list_c)

fileName = "huahuzangpin.json"
fp = open(fileName, 'w', encoding='utf-8')
json.dump(list_c, fp=fp, ensure_ascii=False)
