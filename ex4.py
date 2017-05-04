# variable cars is equal 100
cars = 100
# variable "space_in_a_car" is equal 4.0
space_in_a_car = 4
# variable "drivers" is equal 30
drivers = 30
# variable "passengers" is equal 90
passengers = 90
# variable "cars_not_driven" is equal cars minus drivers
cars_not_driven = cars - drivers
# variable "cars_driven" is equal variable "drivers"
cars_driven = drivers
# variable "carpool_capacity" is equal numbers of cars_driven asterisk(times) space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# variable "average_passengers_per_car" is equal numbers of passengers slash(divide by) cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
