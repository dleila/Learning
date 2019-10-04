# this is an octothorpe -- it makes a comment (line ignored by the computer)
# print("Hello world")
# writing random stuff
print("Howdy, y'all")
# more text
print("I like typing this")
# even more text
print("This is fun")

# math skills demo

# makes a number appear by the text
print("I will not count my chickens", 2)
# does math for you, 30 divided by 6 equals 5 plus 25 equals 30, shows the answer by the hens
print("Hens: ", 25 + 30 / 6)
# does math for you again, the percent sign shows remainders with no fractions
# 25 times 3 equals 75.75 % 4 equals 3.1 minus 3 equals 97
print("Roosters: ", 100 - 25 * 3 % 4)
# another number appears by the text
print("Now I will count the eggs", 7)
# 3 plus 2 plus 1 equals 6 minus 5 equals 1. 4 & 2 equals 0 plus 6 equals 6. 1 minus 0.25 plus 6 equals 6.75.
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# 3 plus 2 equals 5 and 5 minus 7 equals -2. -2 is not greater than 5 so python shows this as false.
print(3 + 2 < 5 - 7)
# 75 minus 15 equals 60. 60 divided by 8 equals 7.5. 4 plus 0.125 minus 7 equals -2.875. 7n5 is greater than -2.875
print(75.0 - 15.0 / 8.0 > 4.0 + 1/8 - 7.0)

# variables and some  of their powers
cars = 80
SpaceInACar = 4.0
drivers = 45
passengers = 115
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = SpaceInACar * cars_driven
average_passengers_per_car = passengers / cars_driven
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available today.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put approximately", average_passengers_per_car, "people in each car.")

vanilla_sold = 20
chocolate_sold = 15
strawberry_sold = 10
carmel_sold = 20
ice_cream_sold = vanilla_sold + chocolate_sold + strawberry_sold + carmel_sold
price_per_ice_cream = 2
total_made = ice_cream_sold * price_per_ice_cream
print("There were", vanilla_sold, "vanilla flavored ice creams sold today.")
print("There were", chocolate_sold, "chocolate flavored ice creams sold today.")
print("There were", strawberry_sold, "strawberry flavored ice creams sold today.")
print("There were", carmel_sold, "carmel flavored ice creams sold today.")
print("We sold a total of", ice_cream_sold, "ice creams today.")
print("It costs", price_per_ice_cream, "dollars for one ice cream.")
print("We made", total_made, "dollars today.")

# More variables and playing with output
myName = "Dahbi"
myAge = 14
myHeight = 65  # inches
myEyes = "Brown"
myHair = "Brown"

print("Let's talk about %s." % myName)
print("She's %d inches tall." % myHeight)
print("She's got %s eyes and %s hair." % (myEyes, myHair))
print("If I add %d and %d, I get %d." % (myAge, myHeight, myAge+myHeight))