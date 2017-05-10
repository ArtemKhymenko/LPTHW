#i = 0
numbers = []

def adding_func(a, incr):
    i = 0
    while i < a:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + incr
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

adding_func(11, 2)

print "The numbers: "

for num in numbers:
    print num
