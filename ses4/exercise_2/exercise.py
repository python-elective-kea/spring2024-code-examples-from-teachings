import os

directory_path = os.getcwd() + '/ses4/exercise_2/os_exercises'

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

print("Type your input:")
user_input = input()

file = open(directory_path + '/file2.txt', 'w')
file.write(user_input)
file.close()