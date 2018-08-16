import uuid

SALES_TAX = .096
ITEM_CATEGORY_INDEX = 0
ITEM_PRICE_INDEX = 1
ITEM_STOCK_QUANTITY_INDEX = 2
ITEM_ORDER_COUNT_INDEX = 3

Menu = {'wings': ['app', 10.00, 20, 0], 'shrimp': ['app', 10.00, 20, 0], 'spring rolls': ['app', 10.00, 20, 0],
        'cheese fries': ['app', 10.00, 20, 0], 'garlic bread': ['app', 10.00, 20, 0], 'calamari': ['app', 10.00, 20, 0],
        'salmon': ['ent', 10.00, 20, 0], 'steak': ['ent', 10.00, 20, 0], 'cheeseburger': ['ent', 10.00, 20, 0],
        'pizza': ['ent', 10.00, 20, 0], 'quesadilla': ['ent', 10.00, 20, 0], 'curry': ['ent', 10.00, 20, 0],
        'cake': ['des', 10.00, 20, 0], 'ice cream': ['des', 10.00, 20, 0], 'brownie': ['des', 10.00, 20, 0],
        'pumpkin pie': ['des', 10.00, 20, 0], 'chocolate': ['ent', 10.00, 20, 0], 'lemon bar': ['des', 10.00, 20, 0],
        'vodka': ['dri', 10.00, 20, 0], 'bourbon': ['dri', 10.00, 20, 0], 'gin': ['dri', 10.00, 20, 0],
        'slushie': ['dri', 10.00, 20, 0], 'beer': ['dri', 10.00, 20, 0], 'tequlia': ['dri', 10.00, 20, 0],
        'fries': ['sid', 10.00, 20, 0], 'chips': ['sid', 10.00, 20, 0], 'guacamole': ['sid', 10.00, 20, 0],
        'beans': ['sid', 10.00, 20, 0], 'macaroni': ['sid', 10.00, 20, 0], 'coleslaw': ['sid', 10.00, 20, 0], }

appetizers = ['wings', 'shrimp', 'spring rolls', 'cheese fries', 'garlic bread', 'calamari']
entrees = ['salmon', 'steak', 'cheeseburger', 'pizza', 'quesadilla', 'curry']
desserts = ['cake', 'ice cream', 'brownie', 'pumpkin pie', 'chocolate', 'lemon bar']
drinks = ['vodka', 'bourbon', 'gin', 'slushie', 'beer', 'tequila']
sides = ['fries', 'chips', 'guacamole', 'beans', 'macaroni', 'coleslaw']


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def print_item_in_order(item):
    print("{:<25s}".format(str(item) + " x" + str(Menu[item][ITEM_ORDER_COUNT_INDEX])), end="")
    print("{:>25s}".format("$" + str(Menu[item][ITEM_ORDER_COUNT_INDEX] * Menu[item][ITEM_PRICE_INDEX])))


def calculate_sales_tax(subtotal):
    return subtotal * SALES_TAX


def print_line(title, amount):
    print("{:<25s}".format(title), end="")
    print("{:>25s}".format("$" + str(amount)))


def print_order():
    print(50*"*")
    print("The Snakes Cafe\n")
    print(f"Order #{uuid.uuid4()}")
    print(50*"=")
    subtotal = 0
    sales_tax = 0
    total = 0
    for item in Menu:
        if Menu[item][ITEM_ORDER_COUNT_INDEX] != 0:
            print_item_in_order(item)
            subtotal += Menu[item][ITEM_ORDER_COUNT_INDEX] * Menu[item][ITEM_PRICE_INDEX]

    print(50*"-")
    print_line("Subtotal", subtotal)
    sales_tax = calculate_sales_tax(subtotal)
    print_line("Sales Tax", sales_tax)
    total = subtotal + sales_tax
    print_line("Total Due", total)


def print_welcome():
    print('***************************************************')
    print('**        Welcome to the Snakes Cafe!            **')
    print('**        Please see our menu below.             **')
    print('**')
    print('**         To quit at any time, type "quit"      **')
    print('***************************************************\n')


def print_menu():
    print('Appetizers')
    print('----------')
    for k in appetizers:
        print(k)
    print()

    print('Entrees')
    print('--------')
    for k in entrees:
        print(k)
    print()

    print('Desserts')
    print('---------')
    for k in desserts:
        print(k)
    print()

    print('Drinks')
    print('-------')
    for k in drinks:
        print(k)
    print()

    print('Sides')
    print('-------')
    for k in sides:
        print(k)
    print()


def print_query():
    print('***************************************************')
    print('**      What would you like to order?            **')
    print('***************************************************')


if __name__ == "__main__":

    print_welcome()
    print_menu()
    print_query()

    while True:
        user_input = input('>').lower()
        parsed = user_input.split()
        if user_input == 'quit' or user_input == 'q':
            quit()
        elif len(parsed) == 1 and parsed[0] == "menu":
            print_menu()
        elif len(parsed) == 1 and parsed[0] == "order":
            print_order()
        elif parsed[0] == "remove":
            if len(parsed) != 2:
                print("Incorrect format for remove item command")
                continue

            if Menu.get(parsed[1]) is None:
                print(f"{parsed[1]} does not exist in menu")
                continue

            if Menu.get(parsed[1])[ITEM_ORDER_COUNT_INDEX] == 0:
                print(f"You do not have {parsed[1]} in your order")
                continue

            Menu[parsed[1]][ITEM_ORDER_COUNT_INDEX] -= 1
            print(f"Removed 1 order of {parsed[1]} from your order")

        else:
            if len(parsed) > 2:
                print("Incorrect format for adding item to order")
            elif len(parsed) == 2:
                if Menu.get(parsed[0]) is None:
                    print(f"{parsed[0]} does not exist in the menu")
                    continue
                if not represents_int(parsed[1]):
                    print(f"{parsed[1]} should be a number")
                    continue

                # if adding item exceeds stock quantity throw error
                if (int(parsed[1]) + Menu.get(parsed[0])[ITEM_ORDER_COUNT_INDEX]) > Menu.get(parsed[0])[
                    ITEM_STOCK_QUANTITY_INDEX]:
                    print(f"Adding {parsed[1]} orders of {parsed[0]} to your order would exceed stock quantity")
                    continue

                Menu.get(parsed[0])[ITEM_ORDER_COUNT_INDEX] += int(parsed[1])
                print(f"Added {parsed[1]} orders of {parsed[0]} to your order")
            elif len(parsed) == 1:
                if Menu.get(parsed[0]) is None:
                    print(f"{parsed[0]} does not exist in the menu")
                    continue
                # if adding item exceeds stock quantity throw error
                if (1 + Menu.get(parsed[0])[ITEM_ORDER_COUNT_INDEX]) \
                        > Menu.get(parsed[0])[ITEM_STOCK_QUANTITY_INDEX]:
                    print(f"Adding an order of {parsed[0]} to your order would exceed stock quantity")
                    continue

                Menu.get(parsed[0])[ITEM_ORDER_COUNT_INDEX] += 1
                print(f"Added 1 order of {parsed[0]} to your order")

            else:
                print("Invalid input")
