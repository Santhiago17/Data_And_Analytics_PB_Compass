# Função que percorre os caracteres de cada linha

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


with open('actors.csv', 'r') as csvfile:
    linhas = csvfile.readlines()

maiorNumeroDeFilmes = 0
atorComMaisFilmes = ""

for linha in linhas[1:]:
    campos = split_csv_line(linha)
    ator = campos[0]
    try:

        numeroDeFilmes = int(float(campos[2].strip()))

        if numeroDeFilmes > maiorNumeroDeFilmes:
            maiorNumeroDeFilmes = numeroDeFilmes
            atorComMaisFilmes = ator

    except ValueError:
        print(
            f"Erro ao converter o número de filmes para o ator/atriz: {ator} com valor: {campos[2].strip()}")


with open('etapa_1.txt', 'w') as arquivo_txt:
    arquivo_txt.write(f"Ator com mais filmes:  {atorComMaisFilmes}\n")
    arquivo_txt.write(f"Numero de filmes: {maiorNumeroDeFilmes}\n")
