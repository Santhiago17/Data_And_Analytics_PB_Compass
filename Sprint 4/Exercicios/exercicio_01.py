with open('number.txt') as f:
    numeros = f.readlines()

numeros = list(map(int,numeros))

pares = list(filter(lambda x: x % 2 == 0, numeros))

pares_ordenados = sorted(pares,reverse=True)
maiores_pares = pares_ordenados[:5]
soma_maiores_pares = sum(maiores_pares)

print(maiores_pares)
print(soma_maiores_pares)
