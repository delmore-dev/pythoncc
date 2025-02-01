#hello admin: make a list of four usernames, including the name admin. print a message to each user. if the user is "admin", request them to see a report
users  = ['admin','jonah','clark','sally',]

#add in if test to see if list is empty
if users:
    for user in users:
        if user == 'admin':
            print ("hello admin, would you like to see a status report?")
        else:
            print (f"greetings {user}")
#if the list is empty, print the message "we need to find some users!"
else:
    print ("We need to find some users!")

#do the following to create a program that simulates how websited ensure that everyone has a unique username:
#make a list of five usernames called current_users
current_users = ['mark','tom','chris','andy','david']

#make another list of 5 names alled new_users. make sure that one or two of the new usernames are in the current_users list
new_users = ['mark','tom','steve','luis','raul',]

#loop through the new_users to see if each username has already been used. if it has, print a message that the person will ened to enter a new username.
#if the username has not been used, print a message saying that the username is available
#make sure your comparison is case insensitive. 

#converting all names to lower:
current_users = [current_user.lower() for current_user in current_users]
new_users = [new_user.lower() for new_user in new_users]

#the comparison
for new_user in new_users:
    if new_user in current_users:
        print (f"{new_user} is already taken, please choose another username.")
    else:
        print (f"the username {new_user} is available.")

#ordinal numbers: store hte numbers 1-9 in a list.abs
numbers = list(range(1,10))
#loop through the list
for number in numbers:
    print (number)
#use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.abs
    if number == 1 :
        print (f"{number}st")
    elif number == 2 :
        print (f"{number}nd")
    elif number == 3 :
        print (f"{number}rd")
    else:
        print (f"{number}th")