import csv
import json
from os import remove

product_list = [{'Name':'Crud Crackers', 'Price':3.99},{'Name':'Trash Toast', 'Price':3.99}, {'Name':'Gabage Gamon','Price':3.99},{'Name':'Watery Waffer','Price':3.99}, {'Name':'Savage Sausage','Price':3.99}, {'Name':'Biffing Beans','Price':3.99},{'Name':'Exotic Eggs','Price': 3.99}]
couriers_list = [{'Name':'Tom', 'Phone Number': '0800 000 1066'},{'Name':'Dick', 'Phone Number': '0800 000 1066'},{'Name':'Andy','Phone Number': '0800 000 1066'},{'Name':'Harry','Phone Number':'0800 000 1066'}]
orders = [{'Order ID': '1', 'Customer Name': 'Vish', 'customer Address': 'london', 'Customer Phone': 'none of your busssiness', 'Courier': 'andy', 'Status': 'pending'}]

def read_product_list_to_csv():
    with open("Product_List.csv", mode='r',newline='') as file: 
        csv_file = csv.DictReader(file) 
        for row in csv_file: 
            print(row)
def write_product_list_to_cv():
    # with open('product_list.csv', 'w') as f: 
    #     # write = csv.writer(f) 
    #     # write.writerow(['Name', 'Price'])
    #     # write.writerow(product_list) 
    
    with open('Product_List.csv', mode='w',newline='') as file: 
        fieldnames = ['Name','Price'] 
        writer = csv.DictWriter(file, fieldnames=fieldnames) 
        writer.writeheader() 
        writer.writerows([{'Name':'Crud Crackers', 'Price':3.99},{'Name':'Trash Toast', 'Price':3.99}, {'Name':'Gabage Gamon','Price':3.99},{'Name':'Watery Waffer','Price':3.99}, {'Name':'Savage Sausage','Price':3.99}, {'Name':'Biffing Beans','Price':3.99},{'Name':'Exotic Eggs','Price': 3.99}])
        # writer.writerow(product for product in product_list )


def read_couriers_list_to_csv():
    with open("Courier_List.csv", mode='r',newline='') as file: 
        csv_file = csv.DictReader(file) 
        for row in csv_file: 
            print(row)
def write_couriers_list_to_csv():
    with open('Couriers_List.csv', mode='w',newline='') as file: 
        fieldnames = ['Name','Phone Number'] 
        writer = csv.DictWriter(file, fieldnames=fieldnames) 
        writer.writeheader() 
        writer.writerows([{'Name':'Tom', 'Phone Number': '0800 000 1066'},{'Name':'Dick', 'Phone Number': '0800 000 1066'},{'Name':'Andy','Phone Number': '0800 000 1066'},{'Name':'Harry','Phone Number':'0800 000 1066'}])

def read_orders_to_csv():
    with open("Orders.csv", mode='r',newline='') as file: 
        csv_file = csv.DictReader(file) 
        for row in csv_file: 
            print(row)

def write_orders_to_csv():
    with open('Orders.csv', mode='w') as file: 
        fieldnames = ['Order ID','Customer Name','customer Address','Customer Phone','Customer Phone','Courier','Status'] 
        writer = csv.DictWriter(file, fieldnames=fieldnames) 
        writer.writeheader() 
        writer.writerows([{'Order ID': '1', 'Customer Name': 'Vish', 'customer Address': 'london', 'Customer Phone': 'none of your busssiness', 'Courier': 'andy', 'Status': 'pending'}])

# def export_product_list_to_csv():
#     latest_product_list = open("Product_List.csv", "w")
#     latest_product_list.write("%s = %s\n"%("product_list", product_list))
#     latest_product_list.close

# def export_courier_list_to_csv():
#     latest_courier_list = open("Courier_List.csv", "w")
#     latest_courier_list.write("%s = %s\n"%("courier_list", couriers_list))
#     latest_courier_list.close


def create_product(product_list):
    name = input('Please Enter the Name of the product\n')
    price= int(input("Please Enter the Price of the product\n"))
    new_product= {
        'Name': name,
        'Customer Name':price,
    }
    product_list.append(new_product)

def update_product(product_list):
    for postion, product in enumerate(product_list):
        print(postion,product)
    answer = int(input('please enter "postion number" of Product you wish to update: \n'))
    for key,value in product[answer].items():
        print(f"{key}:{value}")
        update_value=input("please enter the new Product infomation. leave entry 'blank' to skip\n")
        if update_value == "":
            continue
        else:
            product_list[answer][key]=update_value
    print(product_list[answer])

def remove_product(product_list):
    for postion, product in enumerate(product_list):
        print(postion,product)
    remove_product  = int(input('please enter postion number of Product you wish to remove: \n'))
    product_list.pop(remove_product)
    print(product_list)

def create_new_courier(couriers_list):
    name = input('Please Enter Courier\'s name \n')
    phone_number= int(input("Please Enter Courier's Phone Number\n"))
    new_courier= {
        'Name': name,
        'Phone Number':phone_number,
    }
    couriers_list.append(new_courier)


def update_courier(couriers_list):
    for postion, courier in enumerate(couriers_list):
        print(postion,courier)
    answer = int(input('please enter postion number of the Courier you wish to update: \n'))
    for key,value in couriers_list[answer].items():
        print(f"{key}:{value}")
        update_value=input("please enter new Courier infomations. leave entry 'blank' to skip\n")
        if update_value == "":
            continue
        else:
            couriers_list[answer][key]=update_value
    print(couriers_list[answer])

def remove_courier(couriers_list):
    for postion, courier in enumerate(couriers_list):
        print(postion,courier)
    remove_courier  = int(input('please enter postion number of the courier you wish to remove: \n'))
    couriers_list.pop(remove_courier)
    print(couriers_list)

def create_order(orders):
    orderID = input('Please enter the order ID')
    customer_name = input("please Enter customer's name\n")
    customer_address = input("Please Enter Customer's Address\n")
    customer_phone = input("Please Enter Customer's Phone numer\n")
    courier = input("please Enter Courier's name\n")
    status = input('Please Enter the currrent status of the order')

    order = {
        'Order ID': orderID,
        'Customer Name':customer_name,
        'customer Address':customer_address,
        'Customer Phone': customer_phone,
        'Courier':courier,
        'Status':status
    }
    orders.append(order)

def updateOrder(orders):
    for postion, order in enumerate(orders):
        print(postion,orders)
    answer = int(input('please enter postion number of Orders you wish to update: \n'))
    for key,value in orders[answer].items():
        print(f"{key}:{value}")
        update_value=input("please enter new order infomations. leave entry 'blank' to skip\n")
        if update_value == "":
            continue
        else:
            orders[answer][key]=update_value
    print(orders[answer])


def remove_Order(orders):
    for postion, order in enumerate(orders):
        print(postion,order)
    remove_order  = int(input('please enter postion number of Orders you wish to remove: \n'))
    orders.pop(remove_order)
    print(orders)

def main_menu():
    answer=input("Welcome to the Dodgy Diner's Main Menu \n \nEnter Number \'1\' to see our food menu \nEnter Number \'2\' to view the Courier list\nEnter Number \'3\' to view  Current Orders\n\nEnter number \'0\' to quit application \n")

    if  answer == '0':
        print("thank you for visting our erring establishment")
        return

    elif answer == '1':
        print(product_list)
        print("Enter number \'0\' to go back to Main Menu\n")
        print("Enter number \'1\' to print Food Menu Again\n")
        print("Enter number \'2\' to create new item on menu\n")
        print("Enter number \'3\' to update item on menu\n")
        print("Enter number \'4\' to delete item on menu\n")
        print("Enter number \'5\' to read you current Product lists from a file\n")
        print("Enter Number \'6\' to write your current product list to a file\n")
        product_list_menu()
        
    elif answer == '2':
        print(couriers_list)
        print("Enter number \'0\' to go back to Main Menu\n")
        print("Enter number \'1\' to print couriers list Again\n")
        print("Enter number \'2\' to create new courier  on menu\n")
        print("Enter number \'3\' to update couriers list on menu\n")
        print("Enter number \'4\' to delete courier on menu\n")
        print("Enter Number \'5\' to read your current courier list from a file\n")
        print("Enter Number \'6\' to write your current courier list to a file\n")
        couriers_list_menu()
    
    elif answer == '3':
        print(orders)
        print("Enter number \'0\' to go back to Main Menu\n")
        print("Enter number \'1\' to print couriers list Again\n")
        print("Enter number \'2\' to create a new  order \n")
        print("Enter number \'3\' to edit order\n")
        print("Enter number \'4\' to delete a order \n")
        print("Enter Number \'5\' to read your current orders from a file\n")
        print("Enter Number \'6\' to write your current orders to a file\n")

        order_menu()

    
    






def product_list_menu():
    product_list_choice = input("Please Enter Number here:\n")
    if product_list_choice == '1':
        print(product_list)
        main_menu()
    elif product_list_choice == '2':
        create_product(product_list)
        print(product_list)
        main_menu()
    elif product_list_choice == "3":
        update_product(product_list)
        main_menu()
    elif product_list_choice == '4':
        remove_product(product_list)
        main_menu()
    elif product_list_choice == '5':
        read_product_list_to_csv()
        main_menu()
    elif product_list_choice == '6':
        write_product_list_to_cv()
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
        create_new_courier(couriers_list)
        print(couriers_list)
        main_menu()
    elif couriers_list_choice == "3":
        update_courier(couriers_list)
        main_menu()
    elif couriers_list_choice == '4':
        remove_courier(couriers_list)
        main_menu()
    elif couriers_list_choice == '5':
        read_couriers_list_to_csv()
        main_menu()
    elif couriers_list_choice == '6':
        write_couriers_list_to_csv()
        main_menu()
    else:
        print("\n\nPlease select a number from 1 to 4\n\n")
        main_menu()


def order_menu():
    orders_choice = input("Please Enter Number here:\n")
    if orders_choice == '1':
        print(orders)
        main_menu()
    elif orders_choice == '2':
        create_order(orders)
        main_menu()
    elif orders_choice == '3':
        updateOrder(orders)
        main_menu()
    elif orders_choice == '4':
        remove_Order(orders)
        main_menu()
    elif orders_choice == '5':
        read_orders_to_csv()
        main_menu()
    elif orders_choice == '6':
        write_orders_to_csv()
        main_menu()
    else:
        print("\n\nPlease select a number from 1 to 4\n\n")
        main_menu()

main_menu()




 