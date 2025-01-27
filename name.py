name = "ada lovelace"
#title function takes the name and makes each word start with a capital letter
print(name.title())

#use .lower to store data
print (name.lower())
print (name.upper())


first_name = "ada"
last_name = "lovelace"

#f-strings (format). used to insert variable's value into a string. f goes outside of the first quote
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

message = print(f"Hello, {full_name.title()}!")