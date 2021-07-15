sierra_leone_food = ['Cassava Leaf','Potato Leaf', 'FuFu','Jollof Rice','Pepper Soup',] 

jamacian_food= ['Oxtail','Brown Stew Chicken','Curry  Chicken','Curry Goat','Salt fish'  ]

print("Hello again  Welcome to Omar's & Leroy's Kitchen \n \n \n")
print("To browse our Sierra leone Dishes Please Enter the Number: \'1\' \n")
print("To browse our Jamacian Dishes Please Enter the Number: \'2\'\n")
print("To exit Kitchen Please eEnter the Number \'0\' \n \n ")

answer=(int(input("Please Enter Number here\n")))

if answer == 1:
        print(sierra_leone_food)

if answer == 2 :
        print(jamacian_food)

if answer == 0 :
        print("Thank you for comeing to Omar's & Leroy's Kitchen! \n            We hope to see you soon!\n")