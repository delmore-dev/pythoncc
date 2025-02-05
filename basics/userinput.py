#get user input with the input() function
message = input("Enter your name:")
print(f"Hello, {message}")

#for typing prompts that are longer than one line, use +=
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print (f"Hello, {name}")

#use int() to accept numerical input
age = input("How old are you?")
#print (age + 2) #will return error because input is a string
age = int(age)
print (age + 2)