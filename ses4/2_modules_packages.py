# https://realpython.com/python-import/#packages

import math 
#list contents of namespace
print(dir())
#list contents of math
print(f'\nmath contains: {dir(math)[:3]} and more')

# kun pi fra math, placerer 'pi' et globalt namespace
from math import pi
print(pi)

print('\n--- OS EXERCISES ---')
# Do the following tasks using the os module
import os

# 1. create a folder and name the folder 'os_exercises.'   
os.chdir("/workspaces/spring2024-code-examples-from-teachings/ses4")
print(f'current dir: {os.getcwd()}')

if os.path.isdir("/workspaces/spring2024-code-examples-from-teachings/ses4/os_exercises") == False:
    os.mkdir('os_exercises')


os.chdir('os_exercises')
print(f'current dir: {os.getcwd()}')
print(f'inside it you can find: {os.listdir(path=".")}')

# 2. In that folder create a file. Name the file 'exercise.py'
f = open('exercise.py', 'w')

# 3. get input from the console and write it to the file.
#    Får input fra brugeren
user_input = input("Indtast noget tekst til at gemme i filen: ")

# Åbner filen 'exercise.py' i skrivetilstand ('w') i den nuværende mappe

file = open('exercise.py', 'w')
file.write(user_input)

print("Teksten er gemt i filen 'exercise.py'.")

# 4. repeat step 2 and 3 (name the file something else).
os.chdir("/workspaces/spring2024-code-examples-from-teachings/ses4/os_exercises")
print(f'current dir: {os.getcwd()}')

user_input = input('\nIndtast input til fil nummer 2: ')

with open('exercise2.py', 'w') as file:
    # Skriver brugerens input til filen
    file.write(user_input)

# 5. read the content of the files and and print it to the console.

e1 = open('exercise.py', 'r')
e2 = open('exercise2.py', 'r')

print(f'''\n
Indhold i første: {e1.read()}
Indhold i andre: {e2.read()}
      ''')