#lists go inside brackets. dont forget quotes and commas.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#above doesnt work. use brackets to call a single item:
print(bicycles[0])
print(bicycles[0].title())

#last item is always -1. this can also work with other negative numbers
print(bicycles[-1])
print(bicycles[-3])

#and adding f strings
message = f"my favorite bicycle is a {bicycles[0].title()}"
print(message)