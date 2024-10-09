
animais = [
    "Cachorro", "Gato", "Elefante", "Girafa", "Zebra", 
    "Leão", "Tigre", "Lobo", "Urso", "Panda", 
    "Canguru", "Rinoceronte", "Hipopótamo", "Cavalo", 
    "Águia", "Tartaruga", "Jacaré", "Coelho", "Raposa", "Gorila"
]

animais.sort()

[print(animal) for animal in animais]

with open("animais.csv", "w") as file:
    for animal in animais:
        file.write(f"{animal}\n")
