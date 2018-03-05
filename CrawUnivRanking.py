import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

def printUnivList(ulist, num):
    tplt = "{0:^6}\t{1:^10}\t{2:^10}\t{3:^10}"
    print(tplt.format("排名", "学校名称", "地区", "总分", chr(12288)))    #chr(12288)为中文字符的空格
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))

def main():
    uinfo = []
    url = "http://zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)    
    printUnivList(uinfo, 20)    # 20 univs
main()

'''
result：
  排名  	   学校名称   	    地区    	    总分    
  1   	   清华大学   	    北京    	   95.3   
  2   	   北京大学   	    北京    	   78.6   
  3   	   浙江大学   	    浙江    	   73.9   
  4   	  上海交通大学  	    上海    	   73.1   
  5   	   复旦大学   	    上海    	   66.0   
  6   	 中国科学技术大学 	    安徽    	   61.9   
  7   	   南京大学   	    江苏    	   59.8   
  8   	  华中科技大学  	    湖北    	   59.1   
  9   	   中山大学   	    广东    	   58.6   
  10  	 哈尔滨工业大学  	   黑龙江    	   57.4   
  11  	   同济大学   	    上海    	   56.4   
  12  	   武汉大学   	    湖北    	   55.5   
  13  	   东南大学   	    江苏    	   55.3   
  14  	  西安交通大学  	    陕西    	   54.2   
  15  	 北京航空航天大学 	    北京    	   54.0   
  16  	   南开大学   	    天津    	   53.9   
  17  	   四川大学   	    四川    	   53.3   
  18  	   天津大学   	    天津    	   52.4   
  19  	  华南理工大学  	    广东    	   51.8   
  20  	  北京师范大学  	    北京    	   51.7  
'''