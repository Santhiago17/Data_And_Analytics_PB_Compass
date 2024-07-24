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


with open('actors.csv', 'r') as arquivo_csv:
    linhas = arquivo_csv.readlines()
    
maior_media_receita = 0
atores_ordenados = []

for linha in linhas[1:]:
    campos = split_csv_line(linha.strip())
    
    ator = campos[0]
    try:
        receita_bruta = float(campos[1].strip().replace(',', ''))
        numero_filmes = int(campos[2])
        media_receita = receita_bruta / numero_filmes
        atores_ordenados.append((ator, media_receita))
    except ValueError:
        print(f"Erro ao converter dados para o ator/atriz: {ator}")

atores_ordenados.sort(key=lambda item: item[1],reverse=True)
        
print("Atores ordenados pela média de receita por filme (decrescente):")
for ator, media_receita in atores_ordenados:
    print(f"- {ator} (Média: ${media_receita:.2f})")

with open('etapa_5.txt', 'w') as arquivo_txt:
    arquivo_txt.write("Atores ordenados pela média de receita por filme (decrescente):\n")
    for ator, media_receita in atores_ordenados:
        arquivo_txt.write(f"- {ator} (Media: ${media_receita:.2f})\n")
