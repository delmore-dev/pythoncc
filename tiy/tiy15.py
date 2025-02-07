#write a function called make_shirt() that accepts a size and the text of a message that's printed on the shirt
def make_shirt(size,text):
    """A function to tell shirt sizes and message to be printed on the shirt"""
    print (f"The shirt size is {size}, and you want the shirt to say {text}.")

make_shirt('small', '"I <3 NY"')

#call the function using positional arguments and using keyword arguments
make_shirt(text='this is a large shirt', size = 'large')