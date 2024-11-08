my_dict = {'Dima': 1985, 'Elena': 1992, 'Irina': 1987}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Anna'))
my_dict.update({'Oleg': 2001, 'Egor': 2003})
print(my_dict)
del my_dict['Irina']
print(my_dict)

my_set = {1, 2, 1, 2, 1, 2, 'Яблоко', 42.314}
print(my_set)
print(my_set.add(13))
print(my_set.add((5, 6, 1.6)))
print(my_set)
print(my_set.discard(1))
print(my_set)
