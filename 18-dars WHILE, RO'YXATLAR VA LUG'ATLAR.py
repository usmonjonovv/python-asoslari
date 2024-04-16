# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:50:51 2024

@author: usmonjonv.k
"""
#1-mashq
orders  = []
print('Write your orders there:')
n=1
while True:
    question = f'Your {n}-order:'
    order = input(question)
    orders.append(order)
    next_order = input('Do you want anything else? (yes/no)')
    if next_order == 'yes':
        n+=1
        continue
    else:
        break
print('Your orders')
for every_order in orders:
    print(every_order.title())
#2-mashq
print('List of producs in the store:') 
products = {} 
sign = True
while sign:
    p_name = input('Product name:')
    p_price = input(f"{p_name.title()}'s price:")
    products[p_name] = int(p_price)
    another_product = input('Is there any other new product? (yes/no)\n- ')
    if another_product != 'yes':
        break
print('List of products:')
for name,price in products.items():
    if name != 'bread':
        print(f"{name.title()}-{price} US dollars per kilo")
    else:
        print(f"{name.title()}-{price} US dollars")
#3-mashq
products = {
    'apple':2,
    'bread':4,
    'meat':5,
    'cheese':2,
    'book':1
    }  
orders = []
n = 1
sign = True
while sign:
    question = f'{n}-order: '
    product = input(question)
    orders.append(product)
    if product not in products:
        orders.remove(product)
        print(f'We don\'t have {product}')
    next_order = input('Do you want any other item? (yes/no)\n- ')
    if next_order== 'yes':
        n+=1
        continue
    else:
        break
print('Your orders:')
for o in orders:
    print(o.title())