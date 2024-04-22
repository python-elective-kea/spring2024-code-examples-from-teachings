# https://python-elective-kea.github.io/spring2024/ses2.html#exercises
l = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
t = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
str = 'Hello World Huston we are here'

print(l[1:])

print(l[:2])

print(l[-2:])

print(l[4:5])

print(l[::2]) # fra 0 til alle, skip 2, samme som [0::2]

print(l[::-1])


tupletolist = list(t[1:-1])
print(tupletolist)
