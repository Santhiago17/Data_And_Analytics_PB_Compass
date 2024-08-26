import boto3
import config
import pandas as pd
import io

session = boto3.Session(
    aws_access_key_id=config.aws_acess_key_id,
    aws_secret_access_key=config.aws_secret_access_key,
    aws_session_token=config.aws_session_token
)


s3 = session.client('s3')
bucket_name = 'desafio-sprint-5-santhiago-santos'
file_key = 'produtos_prestadores_hospitalares_PB_versao_final.csv'

# Buffer
csv_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

columns = [
    "ID_REDE", "CD_OPERADORA", "NO_RAZAO", "GR_MODALIDADE", "DE_PORTE", "ID_PLANO",
    "CD_PLANO", "TP_VIGENCIA_PLANO", "CONTRATACAO", "DE_TIPO_CONTRATACAO",
    "DE_TIPO_MODALIDADE_FINM", "SEGMENTACAO_ASSISTENCIAL", "DE_TIPO_ABRANGENCIA_GEOGRAFICA",
    "LG_FATOR_MODERADOR", "DE_SITUACAO_PRINCIPAL", "CD_SITUACAO_PLANO",
    "ID_ESTABELECIMENTO_SAUDE", "CD_CNPJ_ESTB_SAUDE", "CD_CNES", "NM_ESTABELECIMENTO_SAUDE",
    "DE_CLAS_ESTB_SAUDE", "LG_URGENCIA_EMERGENCIA", "DE_TIPO_PRESTADOR", "DE_TIPO_CONTRATO",
    "DE_DISPONIBILIDADE", "CD_MUNICIPIO", "NM_MUNICIPIO", "SG_UF", "DT_VINCULO_INICIO",
    "DT_VINCULO_FIM", "NM_REGIAO", "DT_ATUALIZACAO"
]

# Carregando o CSV em um DataFrame pandas
try:
    df = pd.read_csv(io.StringIO(csv_string), sep=';', names=columns, on_bad_lines='skip', engine='python')
except pd.errors.ParserError as e:
    print(f"Error parsing file: {e}")
    df = pd.read_csv(io.StringIO(csv_string),sep=';',names=columns,dtype=str,skiprows=1,quotechar='"',on_bad_lines='skip',engine='python',low_memory=False)
    
    df = df.apply(lambda x: x.str.strip('" ').strip() if isinstance(x, str) else x)
    

df = df[df['ID_REDE'].str.contains("ID_REDE") == False] 

df['ID_REDE'] = df['ID_REDE'].fillna('').str.strip('"')


for col in columns:
    df[col] = df[col].fillna('').str.strip('"')
    
    
df['CD_SITUACAO_PLANO'] = pd.to_numeric(df['CD_SITUACAO_PLANO'], errors='coerce')
df['DT_VINCULO_INICIO'] = pd.to_datetime(df['DT_VINCULO_INICIO'], format='%Y-%m-%d', errors='coerce')
df['DT_VINCULO_FIM'] = pd.to_datetime(df['DT_VINCULO_FIM'], format='%Y-%m-%d', errors='coerce')
df['DT_ATUALIZACAO'] = pd.to_datetime(df['DT_ATUALIZACAO'], format='%Y-%m-%d', errors='coerce')


#  Operadores lógicos

filtered_df = df.loc[(df['SG_UF'] == 'PB') & (
    df['DE_SITUACAO_PRINCIPAL'] == 'ATIVO COM COMERCIALIZACAO SUSPENSA')]

# Aplicando as modificações de maneira segura
filtered_df = filtered_df.copy()

# Remover colunas inteiramente vazias antes das operações
filtered_df.dropna(axis=1, how='all', inplace=True)

# Agregação

agg_results = filtered_df.agg({
    'ID_ESTABELECIMENTO_SAUDE': 'count',
    'CD_SITUACAO_PLANO': 'mean'
})

#Condicional

filtered_df.loc['URGENCIA_EMERGENCIA'] = filtered_df['LG_URGENCIA_EMERGENCIA'].apply(lambda x: 'SIM' if x == '1' else 'NÃO')

# Conversão
filtered_df.loc['CD_SITUACAO_PLANO'] = pd.to_numeric(filtered_df['CD_SITUACAO_PLANO'], errors='coerce')

# Data
filtered_df.loc['ANO_VINCULO_INICIO'] = pd.to_datetime(filtered_df['DT_VINCULO_INICIO'], errors='coerce').dt.year

# Função String
filtered_df.loc['NO_RAZAO'] = filtered_df['NO_RAZAO'].str.upper()

# Verificar e excluir colunas completamente vazias novamente após operações
filtered_df = filtered_df.dropna(axis=1, how='all')


# Mostra as primeiras linhas do DataFrame resultante
print(filtered_df.head())


# Salva o DataFrame resultante em um novo CSV
filtered_df.to_csv('resultados.csv', index=False)
