# import argv
from sys import argv
# define arguments
script, input_file = argv
# define function with f argument that prints readed f
def print_all(f):
    print f.read()
# define function that do seek operation
def rewind(f):
    f.seek(0)
# define function with two arguments that prints first argument and read by line second
def print_a_line(line_count, f):
    print line_count, f.readline()
# define variable current_file which equal opened input_file
current_file = open(input_file)

print "First let's print the whole file:\n"
# call print_all function with current_file as an argument
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# call rewind function with current_file as an argument
rewind(current_file)

print "Let's print three lines:"

current_line = 1
# call print_a_line function wuth two arguments
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
