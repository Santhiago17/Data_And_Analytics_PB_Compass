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


with open('actors.csv') as csvfile:
    linhas = csvfile.readlines()

total_gross = 0.0
count = 0


for linha in linhas[1:]:
    campos = split_csv_line(linha.strip())
    try:
        gross = float(campos[5].strip())
        total_gross += gross
        count += 1
    except ValueError:
        print(
            f"Erro ao converter o valor da receita bruta: '{campos[5].strip()}'")

media_gross = total_gross / count if count > 0 else 0


with open('etapa_2.txt','w') as arquivo_txt:
    arquivo_txt.write(f'Media da receita bruta dos principais filmes: {media_gross:.2f}')
