from sys import argv

script, user_name = argv

prompt = '>>'  # what does this mean?
# This is the prompting label befor you key info into computer.

print(f'Hi {user_name}! I am {script}script.')
print('I want to ask you some questions.')
print(f'Do you like me {user_name}?')

likes = input(prompt)

print(f'where do you live {user_name}?')
lives = input(prompt)

print('what kind of computer do you use?')
computer = input(prompt)

print(f"""
Alright, you said {likes} about me.
You live in {lives}.
your computer is {computer}.
""")
