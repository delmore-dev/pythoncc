#make a list that includes at least three people you'd like to invite to diner. Then use your list to print a message to each person, inviting them to dinner.
names = ['Will','Joe','Ada','Leon',]
print(f"{names[0]} woud you like to come to dinner?")
print(f"{names[1]} woud you like to come to dinner?")
print(f"{names[2]} woud you like to come to dinner?")
print(f"{names[3]} woud you like to come to dinner?")

#changing guests: you heard one guest couldnt make it. Change it to someone else, and print new messages
names[3] = 'Steve'
print(f"{names[0]} woud you like to come to dinner?")
print(f"{names[1]} woud you like to come to dinner?")
print(f"{names[2]} woud you like to come to dinner?")
print(f"{names[3]} woud you like to come to dinner?")

#more guests. you found a larger table. use insert and append to add guests to the lists
names.append('Jacob')
names.insert(1, 'Carla')
print (names)

#shrinking guest list. now you only have enough room for two guests. use pop to remove guests one at a time
names.pop()
names.pop()
names.pop()
names.pop()
print (names)
print(f"{names[0]} woud you like to come to dinner?")
print(f"{names[1]} woud you like to come to dinner?")

#use del to remove the last two names on the list
del names[0]
del names [0]
print (names)