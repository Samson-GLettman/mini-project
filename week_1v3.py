import csv
import json

product_list = ['Crud Crackers','Trash Toast', 'Gabage Gamon','Watery Waffer']
couriers_list = ['Tom','Dick', 'Andy','Harry']

def read_product_list_to_txt():
    try:
        try_read_product_list = open("Product_List.txt", "r")
    except:
        except_write_product_list = open("Product_List.txt", "w")
        except_write_product_list.write("['Crud Crackers','Trash Toast', 'Gabage Gamon','Watery Waffer']")
        except_write_product_list.close

def read_couriers_list_to_txt():
    try:
        try_read_couriers_list_to_txt = open("Courier_List.txt", "r")
    except:
        except_write_courier_list = open("Courier_List.txt", "w")
        except_write_courier_list.write("['Tom','Dick', 'Andy','Harry']")
        except_write_courier_list.close

def export_product_list_to_txt():
    latest_product_list = open("Product_List.txt", "w")
    latest_product_list.write("%s = %s\n"%("product_list", product_list))
    latest_product_list.close

def export_courier_list_to_txt():
    latest_courier_list = open("Courier_List.txt", "w")
    latest_courier_list.write("%s = %s\n"%("courier_list", couriers_list))
    latest_courier_list.close


def main_menu():
    answer=input("Welcome to the Dodgy Diner's Main Menu \n \nEnter Number \'1\' to see our food menu \n Enter Number \'2\' to view the Courier list\n \nEnter number \'3\' to save you current Product lists \nEnter Number \'4\' to save your current Courier list\n\nEnter number \'0\' to quit application \n")

    if  answer == '0':
        print("thank you for visting our erring establishment")
        return

    elif answer == '4':
        export_courier_list_to_txt()
        main_menu()

    elif answer == '3':
        export_product_list_to_txt()
        main_menu()

    elif answer == '1':
        print(product_list)
        print("Enter number \'0\' to go back to Main Menu\n")
        print("Enter number \'1\' to print Food Menu Again\n")
        print("Enter number \'2\' to create new item on menu\n")
        print("Enter number \'3\' to update item on menu\n")
        print("Enter number \'4\' to delete item on menu\n")
        product_list_menu()

    elif answer == '2':
        print(couriers_list)
        print("Enter number \'0\' to go back to Main Menu\n")
        print("Enter number \'1\' to print couriers list Again\n")
        print("Enter number \'2\' to create new courier  on menu\n")
        print("Enter number \'3\' to update couriers list on menu\n")
        print("Enter number \'4\' to delete courier on menu\n")
        couriers_list_menu()


def product_list_menu():
    product_list_choice = input("Please Enter Number here:\n")
    if product_list_choice == '1':
        print(product_list)
        main_menu()
    elif product_list_choice == '2':
        new_item = input("Enter New Item: \n")
        product_list.append(new_item)
        print(product_list)
        main_menu()
    elif product_list_choice == "3":
        for postion, product in enumerate(product_list,):
            print(postion,product)
        answer = int(input('please enter number of product you wish to update: \n'))
        print(product_list[answer])
        new_product = input("please enter new product entry: \n")
        product_list[answer] = new_product
        print(product_list)
        main_menu()
    elif product_list_choice == '4':
        print(product_list,'\n')
        remove_item = input("Enter Item you want removed from list: \n")
        product_list.remove(remove_item)
        print(product_list)
        main_menu()
    else:
        print("\n\nPlease select a number from 1 to 4\n\n")
        main_menu()


def couriers_list_menu():
    couriers_list_choice= input("Please Enter Number here:\n")
    if couriers_list_choice == '1':
        print(couriers_list)
        main_menu()
    elif couriers_list_choice == '2':
        new_item = input("Enter New Item: \n")
        couriers_list.append(new_item)
        print(couriers_list)
        main_menu()
    elif couriers_list_choice == "3":
        for postion, courier in enumerate(couriers_list,):
            print(postion,courier)
        answer = int(input('please enter postion number of Courier you wish to update: \n'))
        print(couriers_list[answer])
        new_courier = input("please enter new Courier entry: \n")
        couriers_list[answer] = new_courier
        print(couriers_list)
        main_menu()
    elif couriers_list_choice == '4':
        print(couriers_list,'\n')
        remove_courier = input("Enter Courier you want removed from list: \n")
        couriers_list.remove(remove_courier)
        print(couriers_list)
        main_menu()
    else:
        print("\n\nPlease select a number from 1 to 4\n\n")
        main_menu()












main_menu()