def remove_duplicadas(lst):
    return list(set(lst))

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

resultado = remove_duplicadas(lista)
print(resultado)