def soma_string(numeros_string):
    lista_numeros = numeros_string.split(',')
    
    
    lista_numeros = [int(numero) for numero in lista_numeros]
    
    soma = sum(lista_numeros)
    return soma

numeros_string = "1,3,4,6,10,76"

resultado = soma_string(numeros_string)
print(resultado)
