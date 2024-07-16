from datetime import datetime

nome = "Santhiago"
idade = 24

ano_atual = datetime.now().year
ano_100_anos = ano_atual + (100 - idade)

print(ano_100_anos)