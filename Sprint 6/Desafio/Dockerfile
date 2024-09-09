# Usa uma imagem base com Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala a dependência boto3 diretamente
RUN pip install --no-cache-dir boto3

# Copia o script Python para o diretório de trabalho no contêiner
COPY carrega_dados.py .

# Copia os arquivos CSV locais para o diretório de trabalho no contêiner
COPY movies.csv .
COPY series.csv .

# Comando para executar o script Python
CMD ["python", "carrega_dados.py"]

