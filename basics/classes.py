#classes are like blueprints for creating objects. use capital letters to name the class.
class Dog:
    """a simple attempt to model a dog."""
    def __init__(self, name, age): #__init__ is used to to create a new instance of the class. self parameter is included, and goes first
        """initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over" )

#making an instance of the class
my_dog = Dog('Willie', 6) #no need to pass 'self'
print(f"My dog's name is {my_dog.name}")
print(f"{my_dog.name} is {my_dog.age} years old")

#calling methods. methods are like functions of a class
my_dog.roll_over()
my_dog.sit()