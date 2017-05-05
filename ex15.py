# import package argv from sys module
from sys import argv

script, filename = argv
# put opened file to txt variable
txt = open(filename)

print "Here's your file %r:" % filename
# print data from txt file
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
