# Exrcise 004
'''
题目：一个整数，它加上100后是一个完全平方数，它 加上168 还是一个完全平方数，
请问该数是多少？

'''
'''
for i in range(100):
    for j in range(100):
        if ((i*i-100) == (j*j-168)) and ((i*i - 100)>0):
           num = i*i-100
           print(num)
'''


#改编：
'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，
请问该数是多少？
and ((i*i - num1)>0
'''
num1 = 100
num2 = 100+168
maxnum=1
while(2*maxnum-1<=168):  #i^2-(i-1)^2 = 2*i -1 
    maxnum = maxnum +1

for i in range(maxnum):
    for j in range(maxnum):
        if i*i-num1 == (j*j-num2):
            num = i*i - num1
            print(num)



