# 题目：暂停一秒输出，并格式化当前时间。

import time

import time
 
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
 
# 暂停一秒
time.sleep(10)
 
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
