#alien colors: create a variable called alien_color and assign it a value of 'green' 'yellow' or 'red'.
alien_color = 'green'

#write a test statement to test whether the alien's color is green. if it is, print a message that the player just earned 5 points.
if alien_color == 'green':
    print ("You just earned 5 points!")

#write one version of this program that passes the if test and another that fails

if alien_color == 'red':
    pass

#colors 2: choose a color for an alien and write an if-else chain. if the color is green, print 5 points, if yellow, 10 points, and if red, 15 points
alien_color = "yellow"
if alien_color == 'green':
    print ("You just earned 5 points!")
elif alien_color == 'yellow':
    print ("You just earned 10 points!")
elif alien_color == 'red':
    print ("You just earned 15 points!")
else:
    pass


#stages if life:
#if the person is less than 2, print a message that the person is a baby
age = 1
if age < 2:
    print("you're a baby")
#and if greater than 2 but less than 4, message they're  a toddler
elif age >= 2 and age < 4:
    print("you're a toddler")
#if at least 4 but less than 13, they're a kid
elif age >= 4 and age < 13:
    print("you're a kid")
#between 13 and 20, teenager
elif age >=13 and age <20:
    print("you're a teenager")
#between 20 and 65, adult
elif age >= 20 and age < 65:
    print("you're an adult")
#and 65+ elder
elif age >=65:
    print("you're an elder")