
def dividir_lista(lista):
    
    tamanho_parte = len(lista)// 3
    
    
    primeira_parte = lista[:tamanho_parte]
    segunda_parte = lista[tamanho_parte:2*tamanho_parte]
    terceira_parte = lista[2*tamanho_parte:]
    
    
    return primeira_parte,segunda_parte,terceira_parte
    


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1,parte2,parte3 = dividir_lista(lista)

print(parte1,parte2,parte3)
