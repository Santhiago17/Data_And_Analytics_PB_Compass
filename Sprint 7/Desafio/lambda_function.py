import json
import requests
import boto3
import time
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Configuração do cliente S3
s3_client = boto3.client('s3')
bucket_name = 'data-lake-santhiago-santos'

# IDs dos gêneros Romance e Drama
genero_romance = 10749
genero_drama = 18

# Leitura das variáveis de ambiente
api_key = ""



def buscar_series_pelo_genero(genero_id, page=1, data_maxima="2022-12-31"):
    url = "https://api.themoviedb.org/3/discover/tv"  # Alterado para TV
    params = {
        "with_genres": genero_id,
        "sort_by": "first_air_date.desc",  # Alterado para a data de exibição da série
        "page": page,
        "first_air_date.lte": data_maxima  # Alterado para a data de exibição
    }
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer {api_key}"
    }
    


    response = requests.get(url, params=params, headers=headers)
    print(f"Resposta da API: {response.status_code}, {response.text}")
    time.sleep(1)  # Evita exceder o limite de requisições da API
    return response.json()

def salva_dados_no_s3(data, file_index):
    filename = f"series_data_{file_index}.json"  # Alterado para séries
    s3_path = f"Raw/TMDB/TV/JSON/2024/09/24/{filename}"  # Alterado o caminho no S3

    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_path,
            Body=json.dumps(data, ensure_ascii=False, indent=4),
            ContentType='application/json'
        )
        print(f"\n✅ Arquivo salvo com sucesso: {filename}\nLocalização no S3: {s3_path}\n")
    except (NoCredentialsError, PartialCredentialsError):
        print("❌ Erro ao enviar para o S3: Credenciais inválidas ou incompletas.")
    except Exception as e:
        print(f"❌ Erro ao enviar o arquivo para o S3: {e}")

def coleta_dados_e_salva_series(genero_id, data_maxima="2022-12-31"):
    page = 1
    file_index = 1
    series_data = []

    while True:
        try:
            print(f"🔄 Coletando dados da página {page}...")
            data = buscar_series_pelo_genero(genero_id, page, data_maxima)
            total_pages = data.get('total_pages', 1)
            series = data.get('results', [])

            # Filtra as séries para incluir apenas aquelas com os gêneros desejados
            series_filtradas = [
                serie for serie in series
                if set([genero_romance, genero_drama]).intersection(serie.get('genre_ids', []))
                and all(genero in [genero_romance, genero_drama] for genero in serie.get('genre_ids', []))
            ]

            if not series_filtradas:
                print("🔚 Coleta concluída: Nenhuma série encontrada.\n")
                break

            series_data.extend(series_filtradas)

            # Verificar o tamanho dos dados acumulados e salvar se necessário
            tamanho_atual_dados = len(json.dumps(series_data).encode('utf-8')) / (1024 * 1024)
            if tamanho_atual_dados > 10:
                salva_dados_no_s3(series_data, file_index)
                file_index += 1
                series_data = []

            page += 1

            if page >= total_pages:
                print("🔚 Coleta concluída: Atingido o número máximo de páginas.\n")
                break

        except requests.exceptions.Timeout:
            print("⏳ Timeout: A requisição demorou muito para responder.")
            break
        except Exception as e:
            print(f"❌ Erro ao coletar dados: {e}")
            break

    # Salvar quaisquer dados restantes
    if series_data:
        salva_dados_no_s3(series_data, file_index)

def lambda_handler(event, context):
    """
    Função Lambda Handler principal para coletar dados de séries e salvar no S3.
    """
    coleta_dados_e_salva_series(genero_romance)
    coleta_dados_e_salva_series(genero_drama)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
