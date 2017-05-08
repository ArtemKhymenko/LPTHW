# define a function cheese_and_crackers with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# use function with 20 and 30 as arguments
cheese_and_crackers(20, 30)


print "OR, we can use variables from our scripts:"
amount_of_cheese = 10
amount_of_crackers = 50
# use function with two variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# call the function with math operations as arguments
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# call the function with combined arguments(variables and math)
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def one_more_func(ar1, ar2, ar3):
    suum = ar1 + ar2 + ar3
    print "The result: %d" % (suum*2)

one_more_func(1, 2, 3)
one_more_func((22+4), 3, 0)
var1 = 33 + 33
bar2 = 1234
var2 = 876 - 126
one_more_func(var1, bar2, var2)
one_more_func(12, var1, 0)
one_more_func(0, 0, 0)
one_more_func(bar2, bar2, bar2)
one_more_func(var2, var1, var1)
one_more_func(0, 1, 1)
one_more_func(var2, 22, 33)
one_more_func(0, 5, (77 - 2))
