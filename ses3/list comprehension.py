# Create a list of capital letters in the english alphabet
import string
capital_letters = [letter for letter in string.ascii_uppercase ]

print(capital_letters)

# Create a list of capital letter from the english aplhabet, 
# but exclude 4 with the Unicode code point of either 70, 75, 80, 85.

letters = [letter for letter in string.ascii_uppercase if ord(letter) not in [70, 75, 80, 85]]

print(letters)

# Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

letters = [letter for letter in string.ascii_uppercase if 'F' < letter < 'O'][::2]
print(letters)

# løser den lidt forkert da man også skal have med bokstaver med før F og efter O


# Clothes List Comprehension
# From 2 lists, using a list comprehension, create a list containing:
# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), 
# (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

list = [(c, s) for c in colors for s in sizes]
print(list)

# If the tuple pair is in the following list, it should not be added to the comprehension generated list.

sold_out = [('Black', 'm'), ('White', 's')]
list = [(c, s) for c in colors for s in sizes if (c, s) not in sold_out]
print(list)


# Create a list of even numbers from 0 to 20.
print(
    [num for num in range(0,21,2)]
)

# Create a list of squares of numbers from 1 to 10.
print(
    [num**2 for num in range(0,11)]
)

# Create a list of all the vowels in a given string.
print(
    [letter for letter in 'hei hei woow aaa' if letter in 'aeiouvyæøå']
)

# Create a list of common elements in two given lists. (could this be done with the use of another datastructure?)
print(
    [e for e in ['a', 'b', 'c'] if e in ['b', 'c', 'd'] ]
)

# Create a list of words from a given string that have more than 4 and less than 8 letters.
print(
    [word for word in 'tre fire femmmm seeeeeeeeks'.split() if 4 < len(word) < 8]
)

# Flatten this list (using a list comprehension):
list_of_lists = [
    [1, 2, 3],
    [4, 5],
    [6],
    [7, 8, 9],
]

print(
    [num for list in list_of_lists for num in list]
)
