motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#modifying by choosing a position
motorcycles[0] = 'ducati'
print(motorcycles)

#appending to the end
motorcycles.append('honda')
print(motorcycles)

#inserting in the middle. opens a space at # then inserts.
motorcycles.insert(1, 'mitsubishi')
print(motorcycles)

#removing elements
del motorcycles[0]
print(motorcycles)

#popping removes but lets you work with the item after removal.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print (motorcycles)
print (popped_motorcycle)

#pop uses. can be used to pull the last or first item from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_motorcycle = motorcycles.pop(0)
last_motorcycle = motorcycles.pop()
print (f"My first motorcycle was a {first_motorcycle.title()}. My last motorcycle was a {last_motorcycle.title()}.")

#removing a list item by index
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')
print(motorcycles)

#sorting. use the sort()method. this is a PERMANENT change
cars = ['bmw','audi','ford','chevy',]
cars.sort()
print(cars)

#or reverse sort
cars.sort(reverse=True)
print(cars)

#for temporary sorts, use sorted
cars = ['bmw','audi','ford','chevy',]
print (f"Here is the original list: {cars}")
print(f"Here is the sorted list {sorted(cars)}")
print (f"And the original again {cars}")

#for reverse order (and not reverse alphabetical), use reverse() method:
cars = ["ford","chevy","honda","hyundai","bmw","audi",]
cars.reverse()
print (cars)
print (sorted(cars))

#to find a length, use len()
print (len(cars))