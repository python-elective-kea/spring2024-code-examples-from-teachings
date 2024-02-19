# 1. Reading and writing from files
with open('ses4/exercise_1/numbers.dat', 'w') as writer:
    for i in range(1, 101):
        writer.write(str(i) + '\n')

with open('ses4/exercise_1/numbers.dat', 'r') as f:
    for line in f:
        print(line)
