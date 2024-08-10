def pares_ate(n: int):
    return (i for i in range(2, n + 1) if i % 2 == 0)


# Criando um generator para os pares até 10
generator_pares = pares_ate(10)

# Iterando sobre o generator e imprimindo os valores
for par in generator_pares:
    print(par)
