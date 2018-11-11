#1. 测验beautifulsoup
import requests as req
r = req.get("https://www.baidu.com/")

demo = r.text
#print(demo)

from bs4 import BeautifulSoup as BS
soup  = BS(demo,'html.parser')
# print(soup.prettify())


#2 提取HTML中所有URL链接

#思路： 1） 搜索所有<a>标签   2） 解析<a>标签格式，提取href的链接内容


from bs4 import BeautifulSoup as bs
soup = bs(demo,'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
    
