# Programmed by: Lee Anne Y. Angeles

# DIctionary
userInfo = {
    'Lee Anne Angeles' : {'Age':19,'Sex':'Female','Address':'Morong, Rizal','Contact':'09556727785'},
}

# Display a menu of options
print("\n=========== MENU ===========")
print("\n\t1 -> Add Item")
print("\t2 -> Search")
print("\t3 -> Exit")
print("\n============================")

option = int(input("What do you want to do? "))
	
# option 1: Ask personal data for contact tracing
if option == 1:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your home address: ")
    contact = input("Enter your contact number: ")

print(name, age, address, contact)

# Option 2: Search, ask full name then display the record
# Option 3: Ask the user if want to exit or retry.

