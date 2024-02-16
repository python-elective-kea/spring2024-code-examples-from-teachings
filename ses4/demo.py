# åbne og læse en tekstfil

f = open('test.txt', 'r')
str = f.read()
print(str)


# samme, vha contextmanager protocol

with open('test.txt', 'r') as f:
    print(f.read())


# skriv til tekstfil

g = open('test2.txt', 'w')
g.write('''
    ---
    TEKST nr. 2
    ---
        ''')
g = open('test2.txt', 'r')
print(g.read())

# skriv vha contextmanager protocol
with open('test2.txt', 'w') as g:
    g.write('WRITE NR. 2')

g = open('test2.txt', 'r')
print(g.read())