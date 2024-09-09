import boto3
import os 

AWS_ACCESS_KEY_ID = "xxxxxx"
AWS_SECRET_ACCESS_KEY= "xxxxxx"
AWS_SESSION_TOKEN = "xxxxxx"

LOCAL_FILE_PATH_MOVIES = 'movies.csv'
LOCAL_FILE_PATH_SERIES = 'series.csv'

BUCKET_NAME_MOVIES = 'data-lake-santhiago-santos'
BUCKET_NAME_SERIES = 'data-lake-santhiago-santos'

S3_KEY_MOVIES = 'Raw/Local/CSV/Movies/2024/09/02/movies.csv'
S3_KEY_SERIES = 'Raw/Local/CSV/Series/2024/09/02/series.csv'


def cria_bucket(bucket_name):
    s3_client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        aws_session_token= AWS_SESSION_TOKEN
    )
    

    existing_buckets = [bucket['Name'] for bucket in s3_client.list_buckets()['Buckets']]
    if bucket_name in existing_buckets:
        print(f'O bucket "{bucket_name}" já existe')
        
    else:
        try:
            s3_client.create_bucket(Bucket = bucket_name)
        
            print(f'Bucket "{bucket_name}" criado com sucesso.')
        
        except Exception as e:
            print(f'Erro ao criar o bucket "{bucket_name}": {e}')
            
        

def carrega_para_aws_s3(local_file_path,bucket_name,s3_key):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token= AWS_SESSION_TOKEN
        
    )
    
    try:
        s3_client.upload_file(local_file_path,bucket_name,s3_key)
        print(f'Sucesso: {local_file_path} enviado para s3://{bucket_name}/{s3_key}')
    except Exception as e:
        print(f'Erro ao enviar {local_file_path} para o S3: {e}')
        
def main():
    cria_bucket(BUCKET_NAME_MOVIES)
    cria_bucket(BUCKET_NAME_SERIES)

    carrega_para_aws_s3(LOCAL_FILE_PATH_MOVIES,BUCKET_NAME_MOVIES,S3_KEY_MOVIES)
    carrega_para_aws_s3(LOCAL_FILE_PATH_SERIES,BUCKET_NAME_SERIES,S3_KEY_SERIES)

if __name__ == '__main__':
    main()