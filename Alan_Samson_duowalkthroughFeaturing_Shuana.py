products_list = ['crackers', 'biscuits', 'cake']

print('Welcome to the cafe')

def main_menu():
    choice1 = input('Would you like to see our products or would you like to leave our application?\n'
                    'Choose from the following:\n'
                    '0 - Leave Application\n'
                    '1 - To see our products\n')
    
    if (choice1 == '0'):
        print('Thank you for coming to our cafe. See you again!')
    elif (choice1 == '1'):
        print('Here is our selection: ' + str(products_list))
    choice2 = input('Choose from the following:\n'
                    '0 - Add a new item to the list\n'
                    '1 - Update the item list\n'
                    '2 - Remove an item from the list\n'
                    '3 - Show products from the list\n'
                    '4 - Return to the main menu\n')
    if (choice2 == '0'):
        new_item = input('Enter a new item')
        products_list.append(new_item)
        print('Here is your updated list: ' + str(products_list))
        main_menu()

main_menu()