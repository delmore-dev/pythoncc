#values that dont change are immutable, and immutable lists are called tuples. work similarly to lists, but use parentheses instead of brackets.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#this should return an error. commenting out after verifying:
#dimensions[0] = 250

#looping thru tuple
for dimension in dimensions:
    print (dimension)

#to modify a tuple, reassign the variable as a whole
dimensions = (400,100)
print (dimensions[0])
print (dimensions[1])