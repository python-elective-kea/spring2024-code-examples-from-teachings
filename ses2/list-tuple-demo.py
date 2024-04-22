# LIST
names = ['paul', 'ole', 'bjarne', 'rane']
names.append('arne')

print (names)

for i in names:
    print(i)

for i in range(2, 10, 2): # start, stop, step
    print(i)

print(f'paul i names: {"paul" in names}')
print(f'paul har index {names.index("paul")}')

print(f'list length is {len(names)}')

list_to_tuple = tuple(names) # omgør list til tuple
print(list_to_tuple)

print (names + names) # lægger listen til sig selv

print ( names[::2] ) # start : stop : step (hver anden)




# TUPLE
person = ('Paul', 29, 1994, True)
print(person)
for i in person:
    print (i)

print (f'age is {person[1]}')

