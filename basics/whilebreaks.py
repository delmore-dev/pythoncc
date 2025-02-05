#use break to exit immediately
prompt = "\nTell me something and I'll repeat it."
prompt += "\nEnter 'quit' to end the program."

while True:
    city = input(prompt)

    if city == 'quit': 
        break
    else:
        print(f"I'd love to go to {city.title()}!")