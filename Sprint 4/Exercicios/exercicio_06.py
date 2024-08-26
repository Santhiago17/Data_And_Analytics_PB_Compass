def maiores_que_media(conteudo:dict)->list:
    
    media = sum(conteudo.values()) / len(conteudo)
    
    produtos_filtrados = [(nome,preco) for nome, preco in conteudo.items() if preco > media]
    
    produtos_filtrados.sort(key=lambda x: x[1])
    
    return produtos_filtrados