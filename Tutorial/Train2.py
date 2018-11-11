#7. Tuple: A tuple is collection that cannot be modeified.
#  if you want to change the data during program execution, use a list instead of a tuple
'''
x=(1,)
y=(1,2,3,4)

print(x[0])
print(y[3])
print(y[-1])  # print the last one element, count from the back using the minus sign
'''

#8.  Dictionary
'''
k = {'EN':'English','FR':'French'}
print(k['EN'])

#ADD a new element
k['DE']='German'
print(k['DE'])

# A dictionary has no specific order

#remove an element
del k['EN']
print(k)

'''

#9. list & list comprehensions
'''
import math

numbers = [ math.sqrt(x) for x in range(100)] 
print(numbers[-19])

numberarray= [x for x in range(90,100)]
print(numberarray)
'''

#10. for Loop
'''
for i in range(0,10):
    for j in range(92,103):
        print('(',i,',',j,')')
'''

#11. while Loop
'''
x=0

while x!=5:
    x=int(input('guess a number:'))

    if x!=5:
        print('it is incorrect.')
print('You are correct.')
'''

#12. try-except!!!
'''
rawInput=input('Enter a number:')

try:
    x=int(rawInput)
    print(x)
except:
    print('Invalid input specified')
'''

#13. Expanded for Loop : usiing for loop to operate the dictionary
'''
states={

    'A':'123',
    'B':'234',
    'C':'567',
    'D':'789'
    }

for key,value in states.items():
    print('%s.state=%s'%(key,value))
'''

#14. Read files


filename = 'C:/Users/Alex/Desktop/readme.txt'

with open(filename) as fn:
    content = fn.readlines()
print('content = %s' %(content))

content2 = [x.strip() for x in content]
print('content2 = %s' %(content2))


content3= open(filename,'r').read() # read file into string
print('content3 = %s' %(content3))


string={'dsf','sdf','sdfdfggfdgf'}
print(string)



































