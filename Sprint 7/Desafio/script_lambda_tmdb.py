import requests
import json
import boto3
import time
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Configuração das credenciais da AWS diretamente no código
aws_access_key_id = ''
aws_secret_access_key = ''
aws_session_token = ''

# Configuração do cliente S3 com credenciais fornecidas
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token = aws_session_token
)
bucket_name = 'data-lake-santhiago-santos'

api_key = ""

# IDs dos gêneros Romance e Drama
genero_romance = 10749
genero_drama = 18



def buscar_filmes_pelo_genero(genero_id, page=1, data_maxima="2022-12-31"):

    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "with_genres": genero_id,
        "sort_by": "release_date.desc",
        "page": page,
        "release_date.lte": data_maxima
    }
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "
    }

    response = requests.get(url, params=params, headers=headers)
    print(f"Resposta da API: {response.status_code}, {response.text}")
    time.sleep(1)  # Evita exceder o limite de requisições da API
    return response.json()

def salva_dados_no_s3(data, file_index):

    # Define o caminho completo para o arquivo no bucket
    filename = f"filmes_data_{file_index}.json"
    s3_path = f"Raw/TMDB/JSON/2024/09/22/{filename}"

    # Salva o arquivo no bucket S3
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

def coleta_dados_e_salva(genero_id, data_maxima="2022-12-31"):

    page = 1
    file_index = 1
    filmes_data = []

    while True:
        try:
            print(f"🔄 Coletando dados da página {page}...")
            data = buscar_filmes_pelo_genero(genero_id, page, data_maxima)
            total_pages = data.get('total_pages', 1)
            filmes = data.get('results', [])

            # Filtra os filmes para incluir apenas aqueles com os gêneros desejados
            filmes_filtrados = [
                filme for filme in filmes
                if set([genero_romance, genero_drama]).intersection(filme.get('genre_ids', []))
                and all(genero in [genero_romance, genero_drama] for genero in filme.get('genre_ids', []))
            ]

            if not filmes_filtrados:
                print("🔚 Coleta concluída: Nenhum filme encontrado.\n")
                break

            filmes_data.extend(filmes_filtrados)

            # Verificar o tamanho dos dados acumulados e salvar se necessário
            tamanho_atual_dados = len(json.dumps(filmes_data).encode('utf-8')) / (1024 * 1024)
            if tamanho_atual_dados > 10:
                salva_dados_no_s3(filmes_data, file_index)
                file_index += 1
                filmes_data = []
                
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
    if filmes_data:
        salva_dados_no_s3(filmes_data, file_index)

def lambda_handler(event, context):
    """
    Função Lambda Handler principal para coletar dados de filmes e salvar no S3.
    """
    
    coleta_dados_e_salva(genero_romance)
    coleta_dados_e_salva(genero_drama)


