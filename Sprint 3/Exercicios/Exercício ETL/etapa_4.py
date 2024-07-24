def split_csv_line(line):
    fields = []
    field = ''
    inside_quotes = False
    i = 0
    while i < len(line):
        if line[i] == '"':
            inside_quotes = not inside_quotes
        elif line[i] == ',' and not inside_quotes:
            fields.append(field.strip())
            field = ''
        else:
            field += line[i]
        i += 1
    fields.append(field.strip())
    return fields

with open('actors.csv', 'r', encoding='utf-8') as arquivo_csv:
    linhas = arquivo_csv.readlines()

filme_contagem = {}

for linha in linhas[1:]:
    
    campos = split_csv_line(linha.strip())   
    if len(campos) >= 6:
        filme = campos[4].strip()
        if filme in filme_contagem:
            filme_contagem[filme] += 1
        else:
            filme_contagem[filme] = 1
    else:
        print(f"Erro: Linha com menos de 6 campos encontrada: {campos}")


filmes_ordenados = sorted(filme_contagem.items(), key=lambda item: (-item[1], item[0]))


print("Contagem de aparições dos filmes (#1 Movie) em ordem decrescente:")
for filme, contagem in filmes_ordenados:
    print(f"{filme}: {contagem}")
    
    
with open('etapa_4.txt', 'w', encoding='utf-8') as arquivo_txt:
    arquivo_txt.write("Contagem de aparicoes dos filmes (#1 Movie) em ordem decrescente:\n")
    for filme, contagem in filmes_ordenados:
        arquivo_txt.write(f"{filme}: {contagem}\n")