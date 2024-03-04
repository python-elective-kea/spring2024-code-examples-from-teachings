import sqlite3

# Opretter en forbindelse til Zoo databasen. Hvis den ikke eksisterer, oprettes den.
conn = sqlite3.connect('Zoo.db')
c = conn.cursor()

# Opretter Animal tabellen hvis den ikke allerede findes
c.execute('''CREATE TABLE IF NOT EXISTS Animal
             (id INTEGER PRIMARY KEY, name TEXT, species TEXT, age INTEGER)''')

# Indsætter 3 dyr i Animal tabellen
animals = [
    ('Elefant', 'Pattedyr', 10),
    ('Tiger', 'pattedyr', 5),
    ('Pipfugl', 'fugl', 2)
]

c.executemany('INSERT INTO Animal (name, species, age) VALUES (?, ?, ?)', animals)

# Gemmer (commit) transaktionen
conn.commit()

# Læser fra databasen og udskriver dyrene
c.execute('SELECT * FROM Animal')

animals = c.fetchall()
for animal in animals:
    print(animal)

# Lukker forbindelsen til databasen
conn.close()