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


list = {

}

while True:
    order = input('>')
    if order == 'quit':
        quit()
    if order in list:
        list[order] += 1
        print(f' ** {list[order]} order has been added to your order **')
    else:
        list[order] = 1
        print(f'One order of {order} has been added to your order.')
