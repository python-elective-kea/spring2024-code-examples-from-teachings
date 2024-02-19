# Ex: Alphabet List Comprehensions
cap_letter = [chr(i) for i in range(ord('A'), ord('Z')+1)]
print(cap_letter)

cap_letter_exclude = [chr(i) for i in range(
    ord('A'), ord('Z')+1) if i not in [70, 75, 80, 85]]
print(cap_letter_exclude)

cap_letter_exclude_second = [chr(i) for i in range(
    ord('A'), ord('Z')+1) if i not in range(ord('F'), ord('O') + 1, 2)]
print(cap_letter_exclude_second)


# Ex: Clothes List Comprehension
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

clothes_list = [(i, j) for i in colors for j in sizes]

print(clothes_list)

sold_out = [('Black', 'm'), ('White', 's')]

clothes_list_exclude = clothes_list = [
    (i, j) for i in colors for j in sizes if (i, j) not in sold_out]

print(clothes_list)

# Ex: list Comprehension exercises

evens = [i for i in range(0, 21, 2)]
print(evens)

squares = [i**2 for i in range(0, 11)]
print(squares)

s = "flæskesteg"
vowels = [c for c in s if c in ['a', 'e', 'i', 'o', 'u']]
print(vowels)


# Can be done with set
first_list = ['red', 'green', 'yellow', 'blue']
second_list = ['red', 'black', 'purple', 'blue']

commons = [i for i in first_list if i in second_list]
print(commons)

# Ex: Flatten a list
list_of_lists = [
    [1, 2, 3],
    [4, 5],
    [6],
    [7, 8, 9],
]

flatten = [j for i in list_of_lists for j in i]

print(flatten)

# Ex: Sort a Text


def remove_vowels_sorted(s):
    return sorted([i for i in s if i not in ['a', 'e', 'i', 'o', 'u']])


print(remove_vowels_sorted('burger'))

# Ex: Sort a list
l = ['Claus', 'Victor', 'Anders', 'Nicolai', 'Omar']
print(sorted(l))
print(sorted(l, reverse=True))
print(sorted(l, key=len))


def last_letter(s):
    return s[-1]


print(sorted(l, key=last_letter))


def a_in(s):
    return ('a' not in s, s)


print(sorted(l, key=a_in))

# Ex: Text editor plugin simulation
str = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

print(len(str)) 

print(len([char for char in str if char != ' ']))

print(len(str.split(' ')))

# Ex: Sort a list of tuples
t = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

sorted_t = sorted(t, key=lambda x: (x[1], x[0]))

print(sorted_t)

# Ex: Logic if / else

# TODO: create eval system
""" def grade_eval_system(score):
    return

 """

# Ex: And / or logic
