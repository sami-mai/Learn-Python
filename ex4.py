# Exercise 4: Variables and Names
# assign the value 100 to cars; for number of cars
cars = 100
# assign 4.0 to space_in_car; for number of seats
space_in_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
