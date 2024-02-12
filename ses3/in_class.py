# Ex: Alphabet List Comprehensions
cap_letter = [chr(i) for i in range(ord('A'), ord('Z')+1)]
print(cap_letter)

cap_letter_exclude = [chr(i) for i in range(ord('A'), ord('Z')+1) if i not in [70,75,80,85]]
print(cap_letter_exclude)

cap_letter_exclude_second = [chr(i) for i in range(ord('A'), ord('Z')+1) if i not in range(ord('F'), ord('O') + 1, 2)]
print(cap_letter_exclude_second)


# Ex: Clothes List Comprehension
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

clothes_list = [(i,j) for i in colors for j in sizes]

print(clothes_list)

sold_out = [('Black', 'm'), ('White', 's')]

clothes_list_exclude = clothes_list = [(i,j) for i in colors for j in sizes if (i,j) not in sold_out]

print(clothes_list)

# Ex: list Comprehension exercises

evens = [i for i in range(0,21,2)]
print(evens)

squares = [i**2 for i in range(0,11)]
print(squares)

# Ex: Flatten a list


# Ex: Sort a Text


# Ex: Sort a list


# Ex: Text editor plugin simulation


# Ex: Sort a list of tuples


# Ex: Logic if / else


# Ex: And / or logic


# Ex: list and strings exercises