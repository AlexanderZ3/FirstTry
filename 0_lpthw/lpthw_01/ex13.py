from sys import argv

script,first,second,third = argv

print('The script is called:',script)
print('the first  variable is:',first)
print('the second variable is:',second)
print('the third variable is:',third)
t = input('\nplease input a number which you like most:')
print(t,'is you favorite number!----using direct method')
print(f'{t} is your favorite number!---using f-string method')
