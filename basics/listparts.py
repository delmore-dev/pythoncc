players = ["charles","martina","michael","florence","eli",]
#printing 0 to 3
print(players[0:3])

#looping through a slice
print ("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#copying a list
my_foods = ["pizza","cake","beef"]
#must use a colon,, or both lists will be the same. 
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)
#proving different lists
my_foods.append('bread')
friend_foods.append("bacon")

print(my_foods)
print(friend_foods)