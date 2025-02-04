#person: use a dictionary to store information about a person you know. store their fname, lname, age, and city they live in.
person = {'fname' : 'karen', 'lname' : 'smith', 'age' : 32, 'city' : 'springfield'} 
#print each piece of information stored in your dictionary
print (person)

#favorite numbers: use a dictionary to store people's favorite numbers. think of 5 names and use them as keys in the dictionary
#think of a favorite number for each person, and print each person's name and their favorite number
favorite_numbers = {
    'karen' : 26,
    'sally' : 93,
    'brad' : 7,
    'dave' : 56,
    'steve' : 13,
}
print(f"Karens's favorite number is {favorite_numbers['karen']}")
print(f"Sally's favorite number is {favorite_numbers['sally']}")
print(f"Brad's favorite number is {favorite_numbers['brad']}")
print(f"Dave's favorite number is {favorite_numbers['dave']}")
print(f"Steve's favorite number is {favorite_numbers['steve']}")