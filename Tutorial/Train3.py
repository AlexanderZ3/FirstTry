#14. command line argumemnts  (xxx)
'''
import sys

print('Argumemnts:',len(sys.argv))
print('list:',str(sys.argv))

if sys.argv<2:
    print('To few arguments, please specify a filename')

filename = sys.argv[1]
print('filename:',filename)
'''

#15. write file (xxx)
'''
import codecs

f=open('C:/Users/Zezhong/Desktop/1.txt',"w")
f.write("sdfhsdjkf")
f.close
'''


#16.Date and Time
'''
import time

ticks = time.time()
print('ticks since epoch:',ticks)

timenow=time.localtime(time.time())
print("current time:",time)

timenow2=time.asctime(time.localtime(time.time()))
print(timenow2)
'''

#17.isntall modules(xxx)
'''
import math

print(math.pi)
x=math.sin(1)
print(x)

content=dir(math) # to find the aviliable functions in math module
print(content)

'''

#18. import random

'''
import random

list= []
for i in range(0,100):
    x=random.randint(0,10)
    list.append(x)

print(list)

list2=[0,2,5,6,4,5,6,3,9,4]
y=random.sample(list2,3)
print(y)
'''

import sys
from PyQt5 import QtGui


app = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("Hello Qt!")
label.show()

sys.exit(app.exec_())



















