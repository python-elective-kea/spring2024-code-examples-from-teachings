import sqlite3

# sqlite3 er en DB-API 2.0 interface for SQLite databases

# Create a Database called Zoo, with an Animal Table.

con = sqlite3.connect("zoo.db") # opretter connection til on-disk db
cur = con.cursor() # opretter db cursor

cur.execute("DROP TABLE IF EXISTS animal")
cur.execute("CREATE TABLE animal (name TEXT, amount INTEGER)")

# Insert 3 animals
cur.execute("INSERT INTO animal (name, amount) VALUES ('Lion', 2)")
cur.execute("INSERT INTO animal (name, amount) VALUES ('Tiger', 3)")
cur.execute("INSERT INTO animal (name, amount) VALUES ('Bear', 4)")
con.commit() # Gemmer ændringerne i databasen

# Insert 2 more
data = [
    ('Cat', 15),
    ('Dog', 5)
]
cur.executemany("INSERT INTO animal VALUES(?, ?)", data)
con.commit()

# Read from the database and print the animals to the screen.
cur.execute("SELECT * FROM animal")
animals = cur.fetchall()
for animal in animals:
    print(animal)