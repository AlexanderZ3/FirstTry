# the Best learning website without video:      https://pythonprogramminglanguage.com/getting-started/
# Good learning website with tutorial video:    https://pythonprogramming.net/introduction-to-python-programming/
# 菜鸟 python3 learning ：     http://www.runoob.com/python3/python3-tutorial.html
# 菜鸟 python 100例 learning ：http://www.runoob.com/python/python-100-examples.html

# 1. input and output
'''
name = input("enter a name:")
print(name)
x=int(input("How old is this man:"))
print(x)
y=float(input("enter a decimal number:"))
print(y)
'''

# 2. strings
'''
s="HELLO WORLD!"
print(s)
print(s[0]) #print the first element of string s
print(s[1]) #print the second element of string s

print(s[1:5])  # string slcing
'''

# 3. String Split
'''
s='To convert the result to' # here is onlu the '  not " 
parts = s.split(" ")  # here what is in the parenthese is the symbol to split the string, and it will disappear 
print (parts)

s2=" Python string example. We split it using the dot character"
print(s2)
parts2=s2.split('.') # here is onlu the '  not "
print(parts2)
'''

# 4. if statement  !!!!
'''
x= int(input("Guess a number:"))

if x==4:
   print('You guessed corrctly! ')

elif x>4:
   print('You guessed larger than the answer.')

else:
   print('You guessed smaller than the answer') #else wrong?why invalid syntax

print('End of the Game.')
'''

# 5. Boolean !!!!
'''
light = FALSE   # Here causes a problem, it should because the function is not called before
print (light)
'''

# 6. Variables
# Global Variables are always within a module, there is no global variables as there is in C programming language
# Best practics:
'''
Global variables are considered a bad practice because functions can have non-obvious behavior.
Usually you want to keep functions small, staying within the size of the screen. If variables
are declared everywhere throughout the code, it becomes less obvious to what the function does
'''


x=2
price=2.5

#text in variables
word='Hello'
word="Hello"
word='''Hello'''

# operators
x=x+3*2
print(x)

y=x/4
print(y)

#more detailed utput
print('x='+str(x))  # string  nedds a +   ;  this str() function converts the numeric variable to text
print('y=',y)       # number does not need a + but a ,
















































