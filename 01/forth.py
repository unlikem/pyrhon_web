# 访问亚马逊上屏页面
#  通过修改 user-agent 来将爬虫伪装成浏览器
import requests

url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print('ok')
    print(r.text)
except:
    print('no')