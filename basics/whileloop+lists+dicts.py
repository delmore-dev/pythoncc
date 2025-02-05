#to modify a list as you work through it, use a while loop
#start with users that need to be verified, and add an empty list to hold confirmed users
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

#verify each user until no more users. move each unverified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#display all confirmed users.
print ("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#removing all instances of a value in a list
pets = ['fish','dog','lizard','cat','rabbit','cat','gerbil','cat',]
while 'cat' in pets:
    pets.remove('cat')
print (pets)

#filling a dictionary with user input.

responses = {}
#set a flag to keep polling active
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb today?")

    #store the response in the dictionary
    responses[name] = response

    #ask for another poller
    repeat = input("Would you like to let another person respond? (yes/no)")

    if repeat == 'no':
        polling_active = False

#print results.
print("\n ---Poll Results ---")
for name, response in responses.items():
    print (f"{name} would like to climb {response}")