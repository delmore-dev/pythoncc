#key-value pairs. every key is connected to it's value with a colon, and a comma goes between pairs.
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

#adding new kv pairs. also can be used to modify
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#starting with empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#position tracking of alien moving at different speeds
alien_0 = {'x_position' : 0 , 'y_position' : 25 , 'speed' : 'medium'}
print(f"original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else :
    x_increment =3

alien_0['x_position'] = {alien_0['x_position'] + x_increment}

print ({f"New position: {alien_0['x_position']}"})

#removing kv pairs:
del alien_0['x_position']
print(alien_0)

#dictionary of similar objects:
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
}

language = favorite_languages['phil'].title()
print(f"Phil's favorite language is {language}.")

#using get() to access values
alien_0 = {'color' : 'green', 'speed' : 'slow'}
#print(alien_0['points']) #this should return an error
point_value = alien_0.get('points', 'no value assigned') #if 'points' doesn't exist, return 'no value'
print (point_value)