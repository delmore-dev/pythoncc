#defining a function
def greet_user():
    """Display a simple greeting.""" #this is called a dockstring, which describes what the function does
    print ("Hello!")

greet_user()

#passing info to a function

def greet_user(username):
    """Display a simple greeting."""
    print(f"hello, {username.title()}")
greet_user('jesse') #the username is called a parameter, a piece of info the function needs to do its job.
