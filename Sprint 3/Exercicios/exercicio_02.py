numeros = [i for i in range(1,4)]

for numero in numeros:
    if numero % 2 == 0:
        print(f"Par: {numero}")
    else:
        print(f"Impar: {numero}")