#the value that a function returns is called a return value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    #return name to calling line
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print (musician)

#adding optional arguments

def get_formatted_name(first_name, last_name, middle_name=''): #adding middle name as an option, claiming it empty. optionals have to go at the end of the line. can also use the "None" special value.
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    #return name to calling line
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print (musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print (musician)


#returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first':first_name, 'last' : last_name}
    return person
musician = build_person('jimi', 'hendrix')
print (musician)