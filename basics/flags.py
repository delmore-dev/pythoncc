#use flags to define a variable that determines if a program is active
prompt = "\nTell me something and I'll repeat it."
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else: print(message)