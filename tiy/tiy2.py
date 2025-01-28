#Personal message: Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"
name = "eric stevenson"
print (f"Hello {name.title()}, would you like to learn some Python today?")

#use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case
print (name.lower())
print (name.upper())
print (name.title())

#find a quote from a famous person you admire. Print the quote and the name of its author.

print ("I think, therefore I am. - Renee Descartes")

#represent the famous person's name using a variable called famous_person. Then compose your message and represent it with a new variable called message.abs

famous_person = "Renee Descartes"
message = "I think therefore I am."

print (f"{message} - {famous_person}")

#Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Print the name once, so that the whitespace around the name is displayed. Then print the name using each of the three stripping functions.

name = "  Joe Smith   "
print (name)
print (name.lstrip())
print (name.rstrip())
print (name.strip())

#Python has a removesuffix() method. Assign the value 'python_notes.txt to a variable called filename. Then use removesuffix() to display the filename without the extension.abs
filename = 'python_notes.txt'
print (filename.removesuffix('.txt'))