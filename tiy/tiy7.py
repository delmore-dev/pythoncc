#couting to twenty.
for value in range (1,21):
    print (value)

#one million. make a list of the numbers from one to one million, and a for loop to print the numbers
numbers = list(range(1,1000001))
print (numbers)
#use min max and sum on 1-100000
print (min(numbers))
print (max(numbers))
print (sum(numbers))

#odds 1-20
for value in range (1,21,2):
    print (value)

#counting by 3s 3-30. in a list. 
threes = list(range(3,30,3))
print (threes)

#make a list of the first 10 cubes
cubes = []
for value in range (1,11):
    cube = value **3
    cubes.append(cube)
print (cubes)

#cube comprehension
cubes = [value **3 for value in range (1,11)]
print (cubes)
