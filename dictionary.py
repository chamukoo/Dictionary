# Programmed by: Lee Anne Y. Angeles

# DIctionary
userInfo = {
    'Lee Anne Angeles' : {'Age':19,'Sex':'Female','Address':'Morong, Rizal','Contact':'09556727785'},
}

# Display a menu of options
print("\n======================= MENU =========================")
print("\n\t1 -> Add Item")
print("\t2 -> Search")
print("\t3 -> Exit")
print("\n======================================================")

option = int(input("\nWhat do you want to do? "))
	
# option 1: Ask personal data for contact tracing
if option == 1:
    while True:
        print("\n=================== ADD USER INFO ====================")
        name = input("\n\tEnter your name: ")
        age = int(input("\tEnter your age: "))
        sex = input("\tEnter your sex: ")
        address = input("\tEnter your home address: ")
        contact = input("\tEnter your contact number: ")
        print("\n======================================================")

        userInput = {'Age':age,'Sex':sex,'Address':address,'Contact':contact}
        userInfo[name] = userInput

        addAgain = input("Do you want to add another user info? (yes/no): ")
        if addAgain == "yes":
            continue
        else:
            break
            

# Option 2: Search, ask full name then display the record
if option == 2:
    while True:
        searchName = input("Who do you want to search for: ")

        if searchName in userInfo:
            print("Full Name: ", searchName, "\nAge: ", (userInfo[searchName]['Age']),
            "\nSex:", (userInfo[searchName]['Sex']), "\nAddress: ", (userInfo[searchName]['Address']),
            "\nContact: ", (userInfo[searchName]['Contact']))
        else:
            print("No user is found with the provided name: {}".format(searchName))

        
        searchAgain = input("Do you want to search again? (yes/no): ")
        if searchAgain == "yes":
            continue
        else:
            break
        
# Option 3: Ask the user if want to exit or retry.
if option == 3:
    while True:
        print("======================= EXIT =========================")
        exitProgram = input("Are you sure you want to exit the program? (yes/no) :")

        if exitProgram == "yes":
            print("Thank you for using this program!")
            exit()
        elif exitProgram == "no":
            break
        else:
            print("Invalid Input! Please try again.")
            continue
