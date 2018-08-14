import sys

print('***************************************************')
print('**        Welcome to the Snakes Cafe!            **')
print('**        Please see our menu below.             **')
print('**')
print('**         To quit at any time, type "quit"      **')
print('***************************************************\n')

print('Appetizers')
print('---------')
print('Wings')
print('Cookies')
print('Spring Rolls\n')

print('Entrees')
print('--------')
print('Salmon')
print('Steak')
print('Meat Tornado')
print('A Literal Garden\n')

print('Desserts')
print('--------')
print('Ice cream')
print('Cake')
print('Pie\n')

print('Drinks')
print('------')
print('Coffee')
print('Tea')
print('Blood of the Innocent\n')


print('***************************************************')
print('**      What would you like to order?            **')
print('***************************************************')



while True:
    order = input('>')
    if order == 'quit':
        quit()
    elif:
        print(f' ** {order} order has been added to your order **')
