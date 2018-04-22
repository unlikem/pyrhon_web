# 百度搜索
import requests
keyword = "gakki"

try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("fail")
