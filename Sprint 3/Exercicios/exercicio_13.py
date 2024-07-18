file_path = 'arquivo_texto.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

print(content,end='')
