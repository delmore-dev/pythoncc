#positional arguments need to be in the same order as the parameters


def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print (f"I have a/an {animal_type}")
    print (f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet ('gerbil', 'harry')

#keyword arguments consist of a variable name, and value
describe_pet(animal_type='hamster', pet_name='larry')

#setting a default value by defining a parameter in the def line
def describe_pet(pet_name, animal_type='dog' ):
    """Display info about a pet"""
    print (f"I have a/an {animal_type}")
    print (f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')