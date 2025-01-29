#range. use range() function to generate a series of numbers.abs
for value in range (1, 5):
    print(value)

#this is funky for whatever reason. the last value isn't printed. so you have to add one more.abs
for value in range (1,6):
    print (value)

#you can also pass one argument, and the count will start at zero
for value in range (6):
    print (value)

#to add the numbers to a list:
numbers = list(range(1, 6))
print (numbers)

#and to skip numbers, add a third argument for the number skipped.
numbers = list(range(1,10,2))
print (numbers)

#also do math in the ranges. using ** for exponents:

squares = []
for value in range (1,10):
    square = value ** 2
    squares.append(square)

print (squares)

#simple stats

digits = [1,2,3,4,5,6,7,8,9,0]
print (min(digits))
print (max(digits))
print (sum(digits))

#comprehensions. combine the for loop and the creation of new elements into one line
squares = [value**2 for value in range (1,11)]
print (squares)