import random

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

random_list = random.sample(range(500), 50)

random_list = sorted(random_list)
tamanho_lista = len(random_list)

media = sum(random_list) / len(random_list)

if tamanho_lista % 2 == 0:
    mediana = (random_list[tamanho_lista // 2 - 1] + random_list[tamanho_lista // 2]) / 2
else:
    mediana = random_list[tamanho_lista // 2]
    

valor_maximo = max(random_list)
valor_minimo = min(random_list)

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
