"""
Work wants an inventory app that:
-stores data into a file
-uses the command line to add/update/delete/list:
    items:
        id
        name
        condition
        *checked in*
"""

# TODO make a menu print out showing options 




next_id = 0
items = [1, 2, 3]
def menu():
        print("""
    1. list all items
    2. add new item
    3. update item
    4. delete item
    5. exit (by item ID)
    """)
#                   OR
# options = ["1. list all items", "2. add new item"]
# for op in options:
#     print(op)

def list_items(itemId):
    
    for item in items:
        print(item)
    print("in list item function")
    pass

def new_item(itemId):
    global next_id
    name = input("Name:")
    cond = input("Condition: ")
    itemId = input("ID: ")
    itemId = next_id
    next_id += 1
    pass

def update_item(itemId):
    pass

def delete_item(itemId):
    pass

# make the menu questions that grab the data

while True:
    menu()
    choice = int(input("> "))
    if choice == 1:
        list_items()
    if choice == 2:
        pass
    if choice == 3:
        pass
    if choice == 4:
        pass
    if choice == 5:
        exit()
    else: 
        input("Invalid input, give a number\n(Press enter to try again)")






# make the file saving stuff