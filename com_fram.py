import requests

def getHTMLText(url):
    try:
        # kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, timeout=30)   # , headers =kv
        r.raise_for_status()    #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(getHTMLText(url))