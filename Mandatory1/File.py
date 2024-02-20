# Opretter en fil kaldet numbers.dat
with open('numbers.dat', 'w') as file:
    # Skriver tallene fra 1 til 100 til filen
    for number in range(1, 101):
        file.write(f"{number}\n")

# Åbner numbers.dat til læsning
with open('numbers.dat', 'r') as file:
    # Læser hver linje (hvert tal) fra filen
    for line in file:
        number = int(line)  # konverterer til int
        if number % 2 == 0:  # Tjekker om tallet er lige
            print(number)  # Udskriver lige tal
