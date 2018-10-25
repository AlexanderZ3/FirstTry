# Functions can return something

def add(a,b):
    print(f'Adding: {a} + {b}')
    return a+b

def substract(a,b):
    print(f"Substracting: {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"Multiplying: {a} * {b}")
    return a*b

def divide(a,b):
    print(f"Dividing: {a} / {b}")
    return a/b


print(add(substract(3,4),multiply(3,1)))
print(substract(add(divide(34,100),24),1023))

print("please enter a float number:")
x = float(input())
print(add(x,1))
