# while 循环
'''
循环使用 else 语句
在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
'''
 
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")


# 2. for循环
import math as m

for letter in 'Python':     # 第一个实例
   print ('当前字母 :', letter)


fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前水果 :', fruit) 


# 循环中使用 else

for num in range(10,2000):  # 迭代 10 到 20 之间的数字
   for i in range(2,int(m.sqrt(num))+1): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print (num, '是一个质数')
