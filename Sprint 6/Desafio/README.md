### Guia sobre cada etapa e organização das evidências do desafio referente a esta Sprint

Sumário evidências:

* [Arquivo python que lê e carrega os arquivos para o S3](./carrega_dados.py)
* [Arquivo docker utilizado para execução do desafio](./Dockerfile)

------------
* [Criação da imagem utilizada](./Cria%20imagem%20definitivo.png)
* [Dados sendo enviados para o bucket](./Dados%20enviados%20para%20o%20bucket.png)
* [Arquivo Movies no bucket](./movies_CSV.png)
* [Arquivo Series no bucket](./series_csv.png)

------------

```markdown
# Desafio: Carregamento de Arquivos CSV para AWS S3 com Docker

Este documento descreve o processo de criação de um script Python para carregar arquivos CSV locais para um bucket S3 da AWS, a configuração de um contêiner Docker para executar o script e o uso de volumes para manipulação dos arquivos CSV no contêiner.

## Requisitos do Desafio

- Desenvolver um script Python para ler dois arquivos CSV locais.
- Criar buckets no AWS S3 e carregar os arquivos CSV para os buckets.
- Utilizar a biblioteca `boto3` para interagir com o S3.
- Executar o script Python dentro de um contêiner Docker.
- Configurar volumes para permitir que o contêiner acesse os arquivos CSV localmente.
- Persistir o contêiner após a execução do script, sem removê-lo automaticamente.

## Passos Realizados

### 1. Criação do Script Python

O script Python (`carrega_dados.py`) foi desenvolvido para:

- Ler dois arquivos CSV: `movies.csv` e `series.csv`.
- Criar os buckets S3, se ainda não existirem.
- Carregar os arquivos CSV para os buckets correspondentes no S3.

**Código do Script Python:**

```python
import boto3

# Credenciais AWS (já definidas no script)
AWS_ACCESS_KEY_ID = "seu_access_key"
AWS_SECRET_ACCESS_KEY = "seu_secret_key"
AWS_SESSION_TOKEN = "seu_token"

# Caminhos dos arquivos CSV
LOCAL_FILE_PATH_MOVIES = 'movies.csv'
LOCAL_FILE_PATH_SERIES = 'series.csv'

# Nomes dos buckets S3
BUCKET_NAME_MOVIES = 'data-lake-santhiago-santos'
BUCKET_NAME_SERIES = 'data-lake-santhiago-santos'

# Caminhos dos arquivos no S3
S3_KEY_MOVIES = 'Raw/Local/CSV/Movies/2024/09/02/movies.csv'
S3_KEY_SERIES = 'Raw/Local/CSV/Series/2024/09/02/series.csv'

def cria_bucket(bucket_name):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN
    )
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f'Bucket "{bucket_name}" criado com sucesso.')
    except s3_client.exceptions.BucketAlreadyExists:
        print(f'O bucket "{bucket_name}" já existe.')
    except Exception as e:
        print(f'Erro ao criar o bucket "{bucket_name}": {e}')

def carrega_para_aws_s3(local_file_path, bucket_name, s3_key):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN
    )
    try:
        s3_client.upload_file(local_file_path, bucket_name, s3_key)
        print(f'Sucesso: {local_file_path} enviado para s3://{bucket_name}/{s3_key}')
    except Exception as e:
        print(f'Erro ao enviar {local_file_path} para o S3: {e}')

def main():
    cria_bucket(BUCKET_NAME_MOVIES)
    cria_bucket(BUCKET_NAME_SERIES)
    carrega_para_aws_s3(LOCAL_FILE_PATH_MOVIES, BUCKET_NAME_MOVIES, S3_KEY_MOVIES)
    carrega_para_aws_s3(LOCAL_FILE_PATH_SERIES, BUCKET_NAME_SERIES, S3_KEY_SERIES)

if __name__ == '__main__':
    main()

```


### Dockerfile

```markdown

# Imagem base do Python
FROM python:3.12-slim

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando o script Python para o diretório de trabalho do contêiner
COPY carrega_dados.py /app/carrega_dados.py

# Instalando as dependências diretamente no Dockerfile
RUN pip install boto3

# Comando padrão para executar o script Python
CMD ["python", "/app/carrega_dados.py"]

```

### Build da imagem Docker

```bash
docker build -t img_data_lake_aws .

```
### Execução do Container com volume

```bash
docker run \
  -v ~/Desktop/Desafio\ Final:/app \
  img_data_lake_aws

```

