#1. 京东商品信息爬虫
'''
import requests as req
url="https://item.jd.com/6008133.html"
try:
     r_jd =req.get(url)
     r_jd.raise_for_status()
     r_jd.encoding=r_jd.apparent_encoding
     print(r_jd.text[:1000])
except:
    print('爬取失败')
'''

#2 Amzon
'''
#method 1
import requests as req
url="https://www.amazon.com/Samsung-MicroSDXC-Adapter-MB-ME64GA-AM/dp/B06XX29S9Q/ref=sr_1_1?s=specialty-aps&ie=UTF8&qid=1520583117&sr=8-1&dpID=41pa5T0NGKL&preST=_SX300_QL70_&dpSrc=srch"
url_cn='https://www.amazon.cn/dp/B00QLEU0YA/ref=cngwdyfloorv2_recs_0/458-0129045-7953936?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=5MNYCA66S0H6XCZHSW73&pf_rd_r=5MNYCA66S0H6XCZHSW73&pf_rd_t=36701&pf_rd_p=7149a3bb-2ee6-4f99-92eb-d87852365f8c&pf_rd_p=7149a3bb-2ee6-4f99-92eb-d87852365f8c&pf_rd_i=desktop'
try:
    r_Amzon=req.get(url)
    r_Amzon.raise_for_status()
    r_Amzon.encoding= r_Amzon.apparent_encoding
    print(r_Amzon.text[:1000])
except:
    print('爬取失败')

'''

'''
#method 2: change the headers name
# 对于那些有数据保护的网站，可以采用这种改头换面的方式来爬取
import requests as req
url="https://www.amazon.com/Samsung-MicroSDXC-Adapter-MB-ME64GA-AM/dp/B06XX29S9Q/ref=sr_1_1?s=specialty-aps&ie=UTF8&qid=1520583117&sr=8-1&dpID=41pa5T0NGKL&preST=_SX300_QL70_&dpSrc=srch"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r_Amzon = req.get(url,headers=kv)
    r_Amzon.raise_for_status()
    r_Amzon.encoding= r_Amzon.apparent_encoding
    print(r_Amzon.text[:1000])
except:
    print('爬取失败')
'''

#3 baidu  & 360  KEYWORD search
'''
import requests as req
url='https://www.baidu.com/s'
keyword= 'Python'
try:
    kv = {'wd':keyword}
    r_bd = req.get(url,params=kv)
    print(r_bd.request.url)
    r_bd.raise_for_status()
    print(len(r_bd.text))
    #print(r_bd.text[100:2000])
except:
    print('爬取失败')
'''

#4 pic search
'''
import requests as req
import os

url = 'http://image.nationalgeographic.com.cn/2018/0201/20180201114431179.jpg'
root='D:/pics_py/'
path= root +  url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r_pic = req.get(url)
        with open(path, 'wb') as f:
            f.write(r_pic.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已经存在')
except:
    print('爬取图片失败')
'''


#4*  video search !!!!(unsolved!!!!)
'''
import requests as req
import os

url = 'https://youtu.be/PF9Qq4tld0A'
root = "D:/video_py/"
path = root+url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r_video = req.get(url)
       # r_video.raise_for_status()
        with open(path,'wb') as f:
            f.write(r_video.content)
            f,close()
            print('文件保存成功')
    else:
        print('文件已经存在')
except:
    print('爬取失败')
'''

#5 IP 地址查询/手机号归属地查询，借助外部查询网站库：http://ip38.com/ip.php?ip=

'''
import requests as req

url_IP='http://ip38.com/ip.php?ip='
url_shouji = 'http://shouji.ip38.com/'
try:
    r_IP = req.get(url_IP+'www.icourse163.org') #''中要添加待查询网址
    r_IP.raise_for_status()
    r_IP.encoding = r_IP.apparent_encoding
    print(r_IP.text[:10000000000000000000000000000])

    r_shouji = req.get(url_shouji+'13245678932'+'.html')#''中要添加待查询手机号
    r_shouji.raise_for_status()
    r_shouji.encoding = r_shouji.apparent_encoding
    #print(r_shouji.text[0:10000000000000000000000])
except:
    print("爬取失败")
'''



































