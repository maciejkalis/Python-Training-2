"""
An interactive dictionary that allows the user to:
1) Add new definitions
2) Search for existing definitions
3) Delete definitions selected by him

"""

dictionary = {}

print("""Welcome in interactive dictionary! Which action you want to take?
S - search for existing definition.
A - add new definition.
D - delete existing definition
W - show whole dictionary with all keys""")

i = 0

while i < 1:
    action = input("Choose action S/A/D/W: ")

    if action.capitalize() == "S":
        wordToSearch = input("Enter the key you want to search: ")
        wordToSearchCapitalized = wordToSearch.capitalize()

        if wordToSearchCapitalized in dictionary:
            print()
            print(wordToSearchCapitalized, "-", dictionary.get(wordToSearchCapitalized))
            print()

        else:
            y = 0
            while y < 1:
                missingWordAction = input("There is no such key you have entered in dictionary. Do you want to add it? (Yes/No): ")

                if missingWordAction.capitalize() == "Yes":
                    wordToAddDefinition = input("Enter the definition of the word you want to add: ")
                    dictionary.update({wordToSearchCapitalized: wordToAddDefinition})
                    print()
                    print("You have updated the dictionary with following definition:", wordToSearchCapitalized, "-", wordToAddDefinition)
                    print()
                    y += 1

                elif missingWordAction.capitalize() == "No":
                    print("Ok, enter another one.", "\n")
                    y += 1

                else:
                    print("You didn't choose correct action. Choose 'Yes' or 'No'")

    elif action.capitalize() == "A":
        wordToAdd = input("Enter the key you want to add: ")
        wordToAddCapitalized = wordToAdd.capitalize()

        if wordToAddCapitalized in dictionary:
            print("The key you want to add is already in the dictionary with following definition:", "\n")
            print(wordToAddCapitalized, "-", dictionary.get(wordToAddCapitalized))

        else:
            wordToAddDefinition = input("Enter the definition of the word you want to add: ")
            dictionary.update({wordToAddCapitalized: wordToAddDefinition})
            print()
            print("You have updated the dictionary with following definition:", wordToAddCapitalized, "-", wordToAddDefinition)
            print()

    elif action.capitalize() == "D":
        wordToDelete = input("Enter the key you want to delete: ")
        wordToDeleteCapitalized = wordToDelete.capitalize()

        if wordToDeleteCapitalized in dictionary:
            y = 0
            while y < 1:
                print("Do you really want to delete key", "'" + wordToDeleteCapitalized + "'", "from dictionary?")
                deleteYesNo = input("(Yes/No): ")

                if deleteYesNo.capitalize() == "Yes":
                    del (dictionary[wordToDeleteCapitalized])
                    print()
                    print("You have deleted key", "'" + wordToDeleteCapitalized + "'", "with it's definition from dictionary.")
                    print()
                    y += 1

                elif deleteYesNo.capitalize() == "No":
                    print("Ok, the key", "'" + wordToDeleteCapitalized + "'", "will not be deleted.")
                    y += 1

                else:
                    print("You didn't choose correct action. Choose 'Yes' or 'No'")

        else:
            print("There is no key", "'" + wordToDeleteCapitalized + "'", "in the dictionary.")

    elif action.capitalize() == "W":
        print()
        for key in dictionary:
            print(key, "-", dictionary[key], "\n")

    else:
        print("You didn't choose correct action. Try one more time.", "\n")
