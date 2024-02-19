import sqlite3
import os

directory_path = os.getcwd() + '/ses4/exercise_3/'

con = sqlite3.connect(directory_path + "Zoo.db")

cur = con.cursor()

cur.execute("CREATE TABLE animal(name, species, sex, age)")

data = [
    ("Peter Pedal", "Monkey", "male", 12),
    ("Pumba", "Warthog", "male", 8),
    ("Kong Julien", "Lemur", "male", 28),
]

cur.executemany("INSERT INTO animal VALUES(?, ?, ?, ?)", data)

for row in cur.execute("SELECT * FROM animal"):
    print(row)