product_list = ['Crud Crackers','Trash Toast', 'Gabage Gamon','Watery Waffer']


def main_menu():
    answer=input("Welcome to the Dodgy Diner's Main Menu \n \nEnter Number \'1\' to see our food menu \nEnter number \'0\' to quit application \n")



    if  answer == '1':
        print(product_list)
        print("Enter number \'0\' to go back to Main Menu\n")
        print("Enter number \'1\' to print Food Menu Again\n")
        print("Enter number \'2\' to create new item on menu\n")
        print("Enter number \'3\' to update item on menu\n")
        print("Enter number \'4\' to delete item on menu\n")
        product_list_choice = input("Please Enter Number here\n")
    if product_list_choice == '0':
        main_menu()
    if product_list_choice == '1':
        print(product_list)
        main_menu()
    if product_list_choice == '2':
        new_item = input("Enter New Item\n")
        product_list.append(new_item)
        print(product_list)
        main_menu()
    if product_list_choice == '4':
        print(product_list,'\n')
        remove_item = input("Enter Item you want removed from list\n")
        product_list.remove(remove_item)
        print(product_list)
        main_menu()

main_menu()