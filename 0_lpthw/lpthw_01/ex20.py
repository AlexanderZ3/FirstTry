from sys import argv

script, input_file = argv
def print_all(file):
    print(file.read())

def rewind(f):
    f.seek(0) # the seek() function is dealing in bytes, not lines.Each time you do f.seek(0) you’re moving to the start of the fle.

def print_a_line(line_count,file):
    print(line_count,file.readline())  #Inside readline() is code that scans each byte of the fle until it fnds a \n character,
                                       #then stops reading the fle to return what it found so far.

current_file = open(input_file)

print("let's print all file first:\n")
print_all(current_file)

print("Now let's rewind, like a tape:\n")
rewind(current_file)

print("Let's print 3 lines:\n")
current_line = 1
print_a_line(current_line,current_file) # every time when the file.realine() operates, this line will lose
print("**********************************************")
current_line += 1
print_a_line(current_line,current_file)
print("**********************************************")
current_line += 1
print_a_line(current_line,current_file)
# print_all(current_file)
print("**********************************************")

'''
A fle in Python is kind of like an old tape drive on
a mainframe or maybe a DVD player. It has a ”read head,” and you can ”seek” this read head
around the fle to positions, then work with it there. Each time you do f.seek(0) you’re moving
to the start of the fle. Each time you do f.readline() you’re reading a line from the fle and
moving the read head to right after the \n that ends that line.
'''
