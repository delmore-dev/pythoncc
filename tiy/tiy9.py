#hello admin: make a list of four usernames, including the name admin. print a message to each user. if the user is "admin", request them to see a report
users  = ['sally', 'mark', 'sophia', 'admin']

for user in users:
    if user == 'admin':
        print ("hello admin, would you like to see a status report?")
    
    else:
        print (f"greetings {user}")

#add in if test to see if list is empty