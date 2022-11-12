# Programmed by: Lee Anne Y. Angeles

# DIctionary
userInfo = {
    'Lee Anne Angeles' : {'Age':19,'Sex':'Female','Address':'Morong, Rizal','Contact':'09556727712'},
}

def main():
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

            while True:
                addAgain = input("\nDo you want to add another user info? (yes/no): ")
                if addAgain == "yes":
                    break
                elif addAgain == "no":
                    main()
                else:
                    print("Invalid Input! Please try again.")
                    continue
                    

    # Option 2: Search, ask full name then display the record
    if option == 2:
        while True:
            print("\n================== SEARCH USER NAME ==================")
            searchName = input("\nWho do you want to search for: ")

            if searchName in userInfo:
                print("\n\tResult:")
                print(f"\n\t{'Full Name: ': <15s}", searchName)
                print(f"\t{'Age: ': <15s}", (userInfo[searchName]['Age']))
                print(f"\t{'Sex: ': <15s}", (userInfo[searchName]['Sex']))
                print(f"\t{'Address: ': <15s}", (userInfo[searchName]['Address']))
                print(f"\t{'Contact: ': <15s}", (userInfo[searchName]['Contact']))
                print("\n======================================================")
            else:
                print("\nNo user is found with the provided name: {}".format(searchName))
                print("\n======================================================")

            while True:
                searchAgain = input("\nDo you want to search again? (yes/no): ")
                if searchAgain == "yes":
                    break
                elif searchAgain == "no":
                    main()
                else:
                    print("Invalid Input! Please try again.")
                    continue
            
    # Option 3: Ask the user if want to exit or retry.
    if option == 3:
        while True:
            print("======================= EXIT =========================")
            exitProgram = input("\nDo you want to exit the program? (yes/no) :")

            if exitProgram == "yes":
                print("Thank you for using this program!")
                exit()
            elif exitProgram == "no":
                main()
            else:
                print("Invalid Input! Please try again.")
                continue

while True:
    main()