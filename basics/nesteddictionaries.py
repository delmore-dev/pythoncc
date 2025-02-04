#defining some stuff
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

#putting them in a list
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print (alien)

#starting with an empty list
aliens = []

#make 30 aliens
for alien_number in range (30):
    new_alien = {'color' : 'green', 'points': 5, 'speed' : 'slow'}
    aliens.append(new_alien)

#show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)

#show how many aliens have been created:
print(f"total number of aliens is {len(aliens)}")

#modifying aliens
for alien in aliens [:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = "medium"
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)


#list in a dictionary:

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print(f"you ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

#dictionary in a dictionary

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein', 
        'location' : 'princeton'
    },
    'mcurie ' : {
        'first' : 'marie',
        'last' : 'curie', 
        'location' : 'paris',
    }, 
}

for username, user_info in users.items():
    print(f"\nUsername : {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(full_name.title())
    print(location.title())