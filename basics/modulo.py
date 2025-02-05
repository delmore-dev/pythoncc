#the modulo operator divides one number by another and returns the remainder. doesn't tell how many times one number fits.
#use it for even/odd.

4%3
5%3
6%3
7%3

number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)

if number %2 == 0:
    print (f"{number} is an even number")
else:
    print (f"{number} is an odd number")