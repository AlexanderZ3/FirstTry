#python 特殊运算符

# 1. 身份运算符  is

a=[1,2,3]
b=a

if(a==b):
    print('==: '+'true')
else:
    print('==: '+'false')

if(a is b):
    print('is: '+'true')
else:
    print('is: '+'false')

c=a[:]
if(a==c):
    print('==: '+'true')
else:
    print('==: '+'false')

if(a is c):
    print('is: '+'true')
else:
    print('is: '+'false')

# 2. 参与运算符

a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")
 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")

# 3.位运算符


a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b;        # 12 = 0000 1100   按位与
print ("1 - c 的值为：", c)
 
c = a | b;        # 61 = 0011 1101   按位或
print ("2 - c 的值为：", c)
 
c = a ^ b;        # 49 = 0011 0001   按位异或
print ("3 - c 的值为：", c)
 
c = ~a;           # -61 = 1100 0011  按位取反
print ("4 - c 的值为：", c)
 
c = a << 2;       # 240 = 1111 0000  左移
print ("5 - c 的值为：", c)
 
c = a >> 2;       # 15 = 0000 1111   
print ("6 - c 的值为：", c)
