# The fifth installment of warmup exercises for python benniers
# For these warmups we will focus on for loops

#1 | Returning evens and odds, use of f string and .format

integers = range(0,23)

even_integers = 0
odd_integers = 0

for x in integers:
    if x % 2 == 0:
        even_integers += 1
    elif x % 2 == 1:
        odd_integers += 1

print(f'our variable integers contains {even_integers} even numbers')
print('our variable integers contains {} odd numbers'.format(odd_integers))

#2 | Unpacking tuples in a list

mylist = [(1,2),(3,4),(5,6),(7,8)]

for a,b in mylist:
    print(a)
    print(b)
# or
    print(a,b)

#3 | Unpacking tuples in a list

item_prices = [('shirt', 25), ('pants', 50), ('jacket', 80)]

for items, prices in item_prices:
    print(items, prices)

#4 | Lets find the sum of the items from our last list

item_prices = [('shirt', 25), ('pants', 50), ('jacket', 80)]

total = 0

for items, prices in item_prices:
    if prices > 0:
        total += prices

print(f'Your total is {total}')


#5 | Pulling values from a dictionary

dict = {'key1': 'door1', 'key2': 'door2'}

for elements in dict.values():
    print(elements)
