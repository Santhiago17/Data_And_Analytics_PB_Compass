def conta_vogais(texto: str) -> int:

    filtro_vogais = filter(lambda char: char in 'aeiouAEIOU', texto)

    contagem_vogais = len(list(filtro_vogais))

    return contagem_vogais


texto = "Ola mundo, este e um importante teste"
print(conta_vogais(texto))
