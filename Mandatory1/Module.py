import os

# 1. Opretter en mappe kaldet 'os_exercises'
os.makedirs('os_exercises', exist_ok=True) # exist_ok=True gør at mappen ikke bliver oprettet hvis den allerede eksisterer

# 2. I mappen, oprettes en fil kaldet 'exercise.py'
file_path1 = os.path.join('os_exercises', 'exercise.py')

# Bruger 'input()' til at få input fra brugeren og skriv det til 'exercise.py'
user_input1 = input("Indtast noget tekst til exercise.py: ")
with open(file_path1, 'w') as file:
    file.write(user_input1)

# 4. Gentagelse trin 2 og 3, men navngiver filen noget andet, f.eks. 'exercise2.py'
file_path2 = os.path.join('os_exercises', 'exercise2.py')
user_input2 = input("Indtast noget tekst til exercise2.py: ")
with open(file_path2, 'w') as file: 
    file.write(user_input2)

# 5. Læs indholdet af begge filer og udskriv det
def read_and_print_file(file_path):
    with open(file_path, 'r') as file:  
        print(f"Indhold af {file_path}:")
        print(file.read())

read_and_print_file(file_path1)
read_and_print_file(file_path2)

