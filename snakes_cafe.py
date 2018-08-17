import uuid
import argparse
import csv
import sys

SALES_TAX = .096
ITEM_CATEGORY_INDEX = 0
ITEM_PRICE_INDEX = 1
ITEM_STOCK_QUANTITY_INDEX = 2
ITEM_ORDER_COUNT_INDEX = 3
PRICE_IS_NOT_FLOAT_ERROR = -1
STOCK_IS_NOT_INT_ERROR = -2


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def represents_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class Order:

    def __init__(self):
        self.order_UUID = uuid.uuid4()
        self.Menu = {}
        self.appetizers = []
        self.entrees = []
        self.desserts = []
        self.drinks = []
        self.sides = []
        self.numberOrdered = 0

    def initMenu(self):
        self.Menu = {'wings': ['app', 10.00, 20, 0], 'shrimp': ['app', 10.00, 20, 0], 'spring rolls': ['app', 10.00, 20, 0],
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


    def print_item_in_order(self, item):
        print("{:<25s}".format(str(item) + " x" + str(self.Menu[item][ITEM_ORDER_COUNT_INDEX])), end="")
        print("{:>25s}".format("$" + str(self.Menu[item][ITEM_ORDER_COUNT_INDEX] * self.Menu[item][ITEM_PRICE_INDEX])))


    def calculate_sales_tax(self, subtotal):
        return subtotal * SALES_TAX


    def print_line(self, title, amount):
        print("{:<25s}".format(title), end="")
        print("{:>25s}".format("$" + str(amount)))


    def display_order(self):
        print(50*"*")
        print("The Snakes Cafe\n")
        print(f"Order #{self.order_UUID}")
        print(50*"=")
        subtotal = 0
        sales_tax = 0
        total = 0
        for item in self.Menu:
            if self.Menu[item][ITEM_ORDER_COUNT_INDEX] != 0:
                self.print_item_in_order(item)
                subtotal += self.Menu[item][ITEM_ORDER_COUNT_INDEX] * self.Menu[item][ITEM_PRICE_INDEX]

        print(50*"-")
        self.print_line("Subtotal", subtotal)
        sales_tax = self.calculate_sales_tax(subtotal)
        self.print_line("Sales Tax", sales_tax)
        total = subtotal + sales_tax
        self.print_line("Total Due", total)


    def getMenuFromCSV(self, menuCSV):
        if not menuCSV.endswith(".csv"):
            return None
        with open(menuCSV, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if not represents_float(row[2]):
                    return PRICE_IS_NOT_FLOAT_ERROR
                if not represents_int(row[3]):
                    return PRICE_IS_NOT_IN_ERROR
                self.Menu[row[0]] = [row[1], float(row[2]), int(row[3]), 0]
                if "app" in row[1]:
                    self.appetizers.append(row[0])
                elif "ent" in row[1]:
                    self.entrees.append(row[0])
                elif "des" in row[1]:
                    self.desserts.append(row[0])
                elif "dri" in row[1]:
                    self.drinks.append(row[0])
                elif "sid" in row[1]:
                    self.sides.append(row[0])

        return "good"


    def print_menu(self):
        print('Appetizers')
        print('----------')
        for k in self.appetizers:
            print(k)
        print()

        print('Entrees')
        print('--------')
        for k in self.entrees:
            print(k)
        print()

        print('Desserts')
        print('---------')
        for k in self.desserts:
            print(k)
        print()

        print('Drinks')
        print('-------')
        for k in self.drinks:
            print(k)
        print()

        print('Sides')
        print('-------')
        for k in self.sides:
            print(k)
        print()

    def print(self):
        self.display_order()

    def len(self):
        return self.numberOrdered


def print_welcome():
    print('***************************************************')
    print('**        Welcome to the Snakes Cafe!            **')
    print('**        Please see our menu below.             **')
    print('**')
    print('**         To quit at any time, type "quit"      **')
    print('***************************************************\n')


def print_query():
    print('***************************************************')
    print('**      What would you like to order?            **')
    print('***************************************************')


def parse_arguments():
    if not len(sys.argv) > 1:
        return None
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--menu", help="use separate menu")
    args = parser.parse_args()
    return args.menu




def main():
    order = Order()
    menuCSV = parse_arguments()
    if menuCSV is not None:
        return_value = order.getMenuFromCSV(menuCSV)
        if return_value is None:
            print("Menu file should be a .csv file")
            quit()
        elif return_value == PRICE_IS_NOT_FLOAT_ERROR:
            print("A price in the csv menu is not of float type")
            quit()
        elif return_value == STOCK_IS_NOT_INT_ERROR:
            print("A stock number in the csv menu is not of int type")
            quit()
    else:
        order.initMenu()

    print_welcome()
    order.print_menu()
    print_query()

    while True:
        user_input = input('>').lower()
        parsed = user_input.split()
        if user_input == 'quit' or user_input == 'q':
            quit()
        elif len(parsed) == 1 and parsed[0] == "menu":
            order.print_menu()
        elif len(parsed) == 1 and parsed[0] == "order":
            order.display_order()
        elif parsed[0] == "remove":
            if len(parsed) != 2:
                print("Incorrect format for remove item command")
                continue

            if order.Menu.get(parsed[1]) is None:
                print(f"{parsed[1]} does not exist in menu")
                continue

            if order.Menu.get(parsed[1])[ITEM_ORDER_COUNT_INDEX] == 0:
                print(f"You do not have {parsed[1]} in your order")
                continue

            order.Menu[parsed[1]][ITEM_ORDER_COUNT_INDEX] -= 1
            print(f"Removed 1 order of {parsed[1]} from your order")

        else:
            if len(parsed) > 2:
                print("Incorrect format for adding item to order")
            elif len(parsed) == 2:
                if order.Menu.get(parsed[0]) is None:
                    print(f"{parsed[0]} does not exist in the menu")
                    continue
                if not represents_int(parsed[1]):
                    print(f"{parsed[1]} should be a number")
                    continue

                # if adding item exceeds stock quantity throw error
                if (int(parsed[1]) + order.Menu.get(parsed[0])[ITEM_ORDER_COUNT_INDEX]) > order.Menu.get(parsed[0])[
                    ITEM_STOCK_QUANTITY_INDEX]:
                    print(f"Adding {parsed[1]} orders of {parsed[0]} " + \
                            "to your order would exceed stock quantity of " + \
                            f"{order.Menu.get(parsed[0])[ITEM_STOCK_QUANTITY_INDEX]}")
                    continue

                order.Menu.get(parsed[0])[ITEM_ORDER_COUNT_INDEX] += int(parsed[1])
                order.numberOrdered += int(parsed[1])
                print(f"Added {parsed[1]} orders of {parsed[0]} to your order")
            elif len(parsed) == 1:
                if order.Menu.get(parsed[0]) is None:
                    print(f"{parsed[0]} does not exist in the menu")
                    continue
                # if adding item exceeds stock quantity throw error
                if (1 + order.Menu.get(parsed[0])[ITEM_ORDER_COUNT_INDEX]) \
                        > order.Menu.get(parsed[0])[ITEM_STOCK_QUANTITY_INDEX]:
                    print(f"Adding an order of {parsed[0]} " + \
                            "to your order would exceed stock quantity of " + \
                            f"{order.Menu.get(parsed[0])[ITEM_STOCK_QUANTITY_INDEX]}")
                    continue

                order.Menu.get(parsed[0])[ITEM_ORDER_COUNT_INDEX] += 1
                order.numberOrdered += 1
                print(f"Added 1 order of {parsed[0]} to your order")

            else:
                print("Invalid input")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nNext time, type q or quit")
