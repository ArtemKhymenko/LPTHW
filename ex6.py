# variable x equal phrase with decimal 10
x = "There are %d types of people." % 10
# variable binary is equal string "binary"
binary = "binary"
# variable do_not is equal string "don't"
do_not = "don't"
# variable y is equal to string with format characters binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)
# print x variable
print x
# print y variable
print y

# print string with format raw character x
print "I said: %r." % x
# print string with format string character y
print "I also said: '%s'." % y
# variable hilarious is equal logical type False
hilarious = False
# variable joke_evaluation is equal string with format raw element, but without its character
joke_evaluation = "Isn't that joke so funny?! %r"
# print variables joke_evaluation and hilarious
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# print string variables w and e, with + sign, which means concatanate string
print w + e
