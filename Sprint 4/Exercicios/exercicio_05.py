import csv


def processar_notas(arquivo_csv):
    estudantes = []

    with open(arquivo_csv, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            nome = row[0]
            notas = list(map(float, row[1:]))

            tres_maiores_notas = sorted(notas, reverse=True)[:3]

            media = round(sum(tres_maiores_notas) / 3, 2)

            tres_maiores_notas_formatadas = list(
                map(lambda x: int(x) if x.is_integer() else x, tres_maiores_notas))

            estudantes.append((nome, tres_maiores_notas_formatadas, media))

    estudantes.sort(key=lambda x: x[0])

    for nome, notas, media in estudantes:

        notas_str = [str(nota) for nota in notas]
        media_str = f"{media:.2f}" if not media.is_integer() else f"{
            media:.1f}"
        print(f"Nome: {nome} Notas: [{
              ', '.join(notas_str)}] Média: {media_str}")


arquivo_csv = 'estudantes.csv'
processar_notas(arquivo_csv)
