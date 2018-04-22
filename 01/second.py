import requests
import time

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return 'success'
    except:
        return 'fail'

if __name__ == "__main__":
    url = "https://www.baidu.com"
    st = time.perf_counter()
    for i in range(100):
        getHTMLText(url)
    et = time.perf_counter()
    print("爬行100次所用时间：{:.2f}s".format(et - st))