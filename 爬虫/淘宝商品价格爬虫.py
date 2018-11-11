import requests as req
import re

def getHTMLText(url):
    try:
        r = req.get(url)
        r.raise_for_status()
        r.edncoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(ls,html):
    try:
        plt = re.findall(r'\"view_price\":\"[\d.]*\"',html)
        tlt = re.findall(r'\"raw_title\":\".*?\"',html)
        #思考怎么搜索两个关键词，怎么设置正则表达式的关键词表示方法？？？？？
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ls.append([price,title])
    except:
        print('')

def printGoods(ls,up,dn):
    try:
        t='{:^10}\t{:^10}\t{:^10}'
        print(t.format('商品序号','价格','名称'))
        count = 0
        for i in range(len(ls)):
            price = float(ls[i][0])
            if price>dn and price <up :
                count = count+1
                print(t.format(count,ls[i][0],ls[i][1]))
                
        print('There are total %d items'%count)
    except:
        print('')

def main():
        good =   '书包'
        page_num= 30
        #爬30个网页
        lis = []
        price_up = 1500
        price_dn = 500
        #只搜索价格在500-1500之间的
        start_url='https://s.taobao.com/search?q='+good
        for i in range(page_num):
            url=start_url+'&s='+str(44*i)
            html = getHTMLText(url)
            parsePage(lis,html)
        printGoods(lis,price_up,price_dn)

main()
    
    
          
