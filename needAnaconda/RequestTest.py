import requests, json

# 第三方库使用之 requests 强化版本的urllib
anshang = 'http://anshang.ldspring.com/version_1_0_0/Course/lists'
douban = 'https://www.douban.com/'
r = requests.post(anshang, data={'cat_id': '1'}, timeout=2)
print(r.content)
print(r.json().get('data').get('ad_list'))
print(json.dumps(r.json()))

doubanRequest = requests.get(douban, headers={
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(doubanRequest.headers['date'])
print(doubanRequest.cookies['talionnav_show_app'])
