#for loops run once, while loops run as long as a condition is true
current_number = 1 
while current_number <= 5:
    print (current_number)
    current_number += 1

#letting user choose when to quit
prompt = "\nTell me something and I'll repeat it."
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print (message)

