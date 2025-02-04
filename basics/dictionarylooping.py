#defining user
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
}

for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")


#using the keys() function:
favorite_languages = {
    'jen' : 'python' ,
    'sarah' : 'c',
    'edward' : 'rust'
}
for name in favorite_languages.keys():
    print(f"{name.title()}")

#and with values()
for language in favorite_languages.values():
    print(f"{language}")

