import requests as req
import re

def getHTMLText(url):
    try:
        r = req.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error1')
        
def parserHtml(lis,html):
        plist = re.findall(r'\"view_price\":\"[\d.]*\"',html)
        tlist = re.findall(r'\"raw_title\":\"正品.*?\"',html)
        for i in range(len(plist)):
            price = eval(plist[i].split(':')[1])
            title = eval(tlist[i].split(':')[1])
            lis.append([price,title])

def printInfoList(lis,price_up,price_dn):
    try:
        t = '{:^10}\t{:^10}\t{:^30}'
        print(t.format('商品序号','商品价格','商品名称'))
        count = 0
        print(len(lis))
        for i in range(len(lis)):
            price = float(lis[i][0])
            if price<price_up and price>price_dn:
                count = count +1
                print(t.format(count,lis[i][0],lis[i][1]))
    except:
        print(' ')       

def main():
    page_num = 5
    Good = 'zippo'
    start_url='https://s.taobao.com/search?q=' + Good
    lis= []
    price_up = 1500
    price_dn = 500
    for i in range(page_num):
        try:
           url = start_url+ '&s=' +str(44*i)
           html = getHTMLText(url)
           parserHtml(lis,html)
        except:
            continue
    printInfoList(lis,price_up,price_dn)
    

main()
