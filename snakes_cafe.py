import sys

print('***************************************************')
print('**        Welcome to the Snakes Cafe!            **')
print('**        Please see our menu below.             **')
print('**')
print('**         To quit at any time, type "quit"      **')
print('***************************************************\n')

appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat', 'Cheese']
desserts = ['Cake', 'Ice-Cream','Brownies', 'Pumpkin Pie']
drinks = ['Vodka', 'Bourbon', 'Gin', 'Nail Polish Remover']


print('Appetizers')
print('----------')
for app in appetizers:
    print(app)
print('\n')


print('Entrees')
print('--------')
for starter in entrees:
    print(starter)
print('\n')

print('Desserts')
print('---------')
for sweet in desserts:
    print(sweet)
print('\n')

print('Drinks')
print('-------')
for lit in drinks:
    print(lit)
print('\n')

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
        print(f'1 order of {order} has been added to your order.')
