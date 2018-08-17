#snakes-cafe

**Author**: Luther Mckeiver
**Version**: 1.0.0

## Overview
Snakes-Cafe is a terminal based restaurant project allows customers to input what they want and receive their order back from an output in the terminal.

## Getting Started
In order to run this app on your own machine I would go to my github account at @LutherMckeiver and then to the repo named snakes-cafe.

After clone down to your machine. And cd into the project and run in via python3.
$ python3 snakes_cafe.py

## Architecture
In this project I am using python 3.

## API
In this app the only thing you are inputting is the food you would like to order from the restaurant, and the output will be your order back from the terminal.

## Change Log


08-13-2018 9:22pm - Fully functional lab from day 1.
08-13-2017 07:50pm - Now it is fully functional
08-14-2017 11:48pm - Lab 2 was finished.


##Features
- [X] When ran, the program should print menu for the restaurant
- [X] The restaurant’s menu should include appetizers, entrees, desserts, and beverages.
- [X] The program should prompt the user for an order
- [X] The program should tell the user how to exit
##  New Features
- [X] Every menu category should have at least 12 items
- [X] Create an Order class. Whatever means you were using to build orders before, replace them with methods and attributes belonging to this class.
- [X] Every Order should have a uuid
- [X] Every Order should have an add_item method that takes an item name and a quantity as arguments. There should be a default value for quantity if none is given.
- [X] Every Order should have a remove_item method that takes an item name and a quantity as arguments. There should be a default value for quantity if none is given.
- [X] Every Order should have a display_order() method that prints the user’s current order to the console
Every Order should have a print_receipt() method that creates a file containing the text of the user’s full order. The file name should be of the format order-<the uuid>.txt and should have the same output as display_order
- [X] All of the order input-checking that you used to do will be done by this class
- [X] The repr of Order instances should look like <Order #ba99d8... | Items: 4 | Total: $754.23>
- [X] When print() is called on an order instance, the user’s current order is printed as if display_order was called.
- [X] When len() is called on an order instance, the number of items in the order is returned
- [X] You may have as many helper methods as you want. However, make sure that any attributes and methods that aren’t intended for public use are prefixed with a single underscore
- [X] All of your methods should be narrow in scope

