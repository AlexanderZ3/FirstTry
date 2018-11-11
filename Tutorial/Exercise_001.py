# Exercise 001
'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

lis=[1,2,3,4]
num = len(lis)*(len(lis)-1)*(len(lis)-2)
print('共有%d个数。'%num)
print('\n他们分别是：\n')
for i in range(len(lis)):
    for j in range(len(lis)):
        for k in range(len(lis)):
            if (lis[i]!=lis[j])and (lis[j]!=lis[k]) and (lis[i]!=lis[k]):
                print('%d'%(lis[i]*100+lis[j]*10+lis[k]))
       
