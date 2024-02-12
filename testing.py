
print(f'{[i for i in range(10)]}')

print([i for i in range(10)])

# sorting
a = ['ccc', 'aaaa', 'd', 'bb']
a[1] = 'aaaz'
print(sorted(a))
print(sorted(a, key=len)) # sort by length

# now sort by the *last* char in the strings:
def Last(s): return s[-1] # defines a function that returns the last char in str
print(sorted(a, key=Last))

# join and split
b = '-'.join(a) # joins the list seperated by whats in the ''
print(b)
print(b.split('-')) # separates the string back to a list by whats in the ''

result = []
for s in a: result.append(s)
print(result)

# range
print(f'range: {range(20)}') # in video, it prints a list

# tuples - fixed size and immutable. content can't be changed
a = (1, 2, 3)
print(len(a))

# list of tuples
a = [(1, 'b'), (2, 'a'), (1, 'a')]
print(a)

print(sorted(a)) # sorts by the 1st, then 2nd part of the tuple'

# tuple, parallell assignment
(x, y) = (1, 2) # assigns 1 to x, and 2 to y
print(f'x: {x}, y: {y}')

# list comprehension and filter
fruits = "Banana pear PEACH strawberry tomato".split()
upper_cased = []
for word in fruits:
    if word.islower():
        upper_cased.append(word.upper())

print(upper_cased)

upper_cased = [word.upper() for word in fruits if word.islower()]

print(upper_cased)