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
ator_com_maior_media_receita = ""

for linha in linhas[1:]:
    campos = split_csv_line(linha.strip())
    
    ator = campos[0]
    try:
        media_receita = float(campos[3].strip().replace(',', ''))
        
        if media_receita > maior_media_receita:
            maior_media_receita = media_receita
            ator_com_maior_media_receita = ator
    except ValueError:
        print(f"Erro ao converter a média de receita para o ator/atriz: {ator} com valor: '{campos[3].strip()}'")

with open('etapa_3.txt', 'w') as arquivo_txt:
    arquivo_txt.write(f'Ator/Atriz com maior media de receita por filme: {ator_com_maior_media_receita}\n')
    arquivo_txt.write(f'Media de receita por filme: {maior_media_receita:.2f}\n')