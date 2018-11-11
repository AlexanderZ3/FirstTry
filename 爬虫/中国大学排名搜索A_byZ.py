import requests as req
from bs4 import BeautifulSoup as BS
import bs4


def getHtml(url):
   try:
       r = req.get(url)
       r.raise_for_status()
       r.encoding=r.apparent_encoding
       return r.text
   except:
       return " "


def uinfolist(html,uinfolist):
    soup = BS(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):# bs4.element.Tag是什么？？？
            tds=tr('td')
            uinfolist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])# append()方法  
          # uinforlist是一个二维数组
def printUlist(ulist,num):
    print('{:^10}\t{:<10}\t{:^10}\t{:^10}'.format('学校排名','学校名称','所在省市','综合得分'))
    for i in range(num):
        u=ulist[i]
        print('{:^10}\t{:<10}\t{:^10}\t{:^10}'.format(u[0],u[1],u[2],u[3])) #10个占位符，^中间对齐，<左对齐 
        
        #print('{:^10}\t{:<10}\t{:^10}\t{:^10}'.format(ulist[i][0],ulist[i][1],ulist[i][2],ulist[i][3]))
        #输出的方法二 利用了 上述二维数组的特性
        
def main():
    ulist = []
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    html = getHtml(url)
    uinfolist(html,ulist)
    printUlist(ulist, 20) # top 20 univs
main()



# 知识点
#1. format()函数的使用：
'''
相对基本格式化输出采用‘%’的方法，format()功能更强大，该函数把字符串当成一个模板，
通过传入的参数进行格式化，并且使用大括号‘{}’作为特殊字符代替‘%’。
##  http://blog.csdn.net/wchoclate/article/details/42297173  ##
<(默认)左对齐    >  右对齐      ^中间对齐     =（只用于数字）在小数点后补齐
'''

2. # append()   >>>>>>>>>>>>   list.appen(obj)
''' 
该方法用语在列表末尾添加新的对象， 无返回值，但是会修改原来的列表。
append()方法向列表的尾部添加一个新的元素，只接受一个参数；  extend()方法只接受一个列表作为参数，
并将该参数的每一个元素都添加到原有的列表中。
'''







