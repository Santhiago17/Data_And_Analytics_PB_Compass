A base de dados analisada refere-se a informações detalhadas sobre produtos e prestadores hospitalares no estado da Paraíba (PB), retiradas de uma base de dados pública disponibilizada pelo governo brasileiro. Ela contém registros que relacionam operadoras de saúde, seus planos, e os estabelecimentos de saúde associados, incluindo hospitais e clínicas.

### Link para base de dados utilizada.

- O Link leva para um arquivo zip com todos os estados, porém o estado utilizado para análise foi o da Paraíba.

https://dados.gov.br/dados/conjuntos-dados/produtos-e-prestadores-hospitalares		

### Sumário

[Arquivo de configuração de credenciais AWS](./config.py)
[Arquivo python com as respectivas consultas e tratamento de dados](./script-s3.py)
[Arquivo CSV com resultado das consultas](./resultados.csv)


## 1. Importação de Bibliotecas

```python
import boto3
import config
import pandas as pd
import io

```

**Descrição**:

- **boto3**: Biblioteca para interagir com os serviços AWS, usada aqui para acessar o bucket S3.
- **config**: Módulo personalizado que contém as credenciais AWS para configurar a sessão.
- **pandas**: Biblioteca para manipulação de dados em Python, usada para processamento e análise de dados.
- **io**: Biblioteca padrão para manipulação de fluxos de dados em memória, usada para converter strings de dados em objetos que pandas pode processar.

## 2. Configuração da Sessão AWS

```python
session = boto3.Session(
    aws_access_key_id=config.aws_acess_key_id,
    aws_secret_access_key=config.aws_secret_access_key,
    aws_session_token=config.aws_session_token
)
```

**Descrição**:

- **boto3.Session**: Cria uma sessão para interagir com a AWS usando as credenciais fornecidas no arquivo `config`.

## 3. Conexão com o S3 e Leitura do Arquivo CSV

```python
s3 = session.client('s3')
bucket_name = 'desafio-sprint-5-santhiago-santos'
file_key = 'produtos_prestadores_hospitalares_PB_versao_final.csv'

# Buffer
csv_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

```

**Descrição**:

- **session.client('s3')**: Conecta-se ao serviço S3 da AWS.
- **get_object**: Recupera o arquivo CSV armazenado no bucket S3.
- **decode('utf-8')**: Decodifica o conteúdo do arquivo para o formato de string UTF-8, tornando-o legível pelo pandas.

## 4. Definição das Colunas do DataFrame

```python
columns = [
    "ID_REDE", "CD_OPERADORA", "NO_RAZAO", "GR_MODALIDADE", "DE_PORTE", "ID_PLANO",
    "CD_PLANO", "TP_VIGENCIA_PLANO", "CONTRATACAO", "DE_TIPO_CONTRATACAO",
	    "DE_TIPO_MODALIDADE_FINM", "SEGMENTACAO_ASSISTENCIAL","DE_TIPO_ABRANGENCIA_GEOGRAFICA",
    "LG_FATOR_MODERADOR", "DE_SITUACAO_PRINCIPAL", "CD_SITUACAO_PLANO",
    "ID_ESTABELECIMENTO_SAUDE", "CD_CNPJ_ESTB_SAUDE", "CD_CNES", "NM_ESTABELECIMENTO_SAUDE",
    "DE_CLAS_ESTB_SAUDE", "LG_URGENCIA_EMERGENCIA", "DE_TIPO_PRESTADOR", "DE_TIPO_CONTRATO",
    "DE_DISPONIBILIDADE", "CD_MUNICIPIO", "NM_MUNICIPIO", "SG_UF", "DT_VINCULO_INICIO",
    "DT_VINCULO_FIM", "NM_REGIAO", "DT_ATUALIZACAO"
]
```

**Descrição**:

- **columns**: Lista que define os nomes das colunas do DataFrame que será criado a partir do CSV. Esta lista garante que as colunas sejam corretamente identificadas ao carregar os dados.

## 5. Carregamento e Tratamento Inicial do DataFrame

```python
try:
    df = pd.read_csv(io.StringIO(csv_string), sep=';', names=columns, on_bad_lines='skip', engine='python')
except pd.errors.ParserError as e:
    print(f"Error parsing file: {e}")
    df = pd.read_csv(io.StringIO(csv_string),sep=';',names=columns,dtype=str,skiprows=1,quotechar='"',on_bad_lines='skip',engine='python',low_memory=False)
    
    df = df.apply(lambda x: x.str.strip('" ').strip() if isinstance(x, str) else x)
```

**Descrição**:

- **pd.read_csv**: Carrega os dados do CSV em um DataFrame do pandas.
- **io.StringIO(csv_string)**: Converte a string CSV em um buffer que pandas pode ler.
- **on_bad_lines='skip'**: Ignora linhas malformadas durante a leitura do CSV.
- **try/except**: Tenta carregar o CSV diretamente e, em caso de erro, executa uma segunda tentativa com tratamento especial para aspas e caracteres indesejados.

## 6. Remoção de Linhas e Tratamento de Colunas

```python
df = df[df['ID_REDE'].str.contains("ID_REDE") == False] 

df['ID_REDE'] = df['ID_REDE'].fillna('').str.strip('"')

for col in columns:
    df[col] = df[col].fillna('').str.strip('"')
```

**Descrição**:

- **Remoção de Linhas Inválidas**: Remove qualquer linha onde o valor da coluna `ID_REDE` contenha o cabeçalho (possível duplicação ou erro).
- **Limpeza de Aspas**: Remove aspas indesejadas em todas as colunas, garantindo que os valores estejam limpos para análises subsequentes.

## 7. Conversão de Tipos de Dados

```python
df['CD_SITUACAO_PLANO'] = pd.to_numeric(df['CD_SITUACAO_PLANO'], errors='coerce')
df['DT_VINCULO_INICIO'] = pd.to_datetime(df['DT_VINCULO_INICIO'], format='%Y-%m-%d', errors='coerce')
df['DT_VINCULO_FIM'] = pd.to_datetime(df['DT_VINCULO_FIM'], format='%Y-%m-%d', errors='coerce')
df['DT_ATUALIZACAO'] = pd.to_datetime(df['DT_ATUALIZACAO'], format='%Y-%m-%d', errors='coerce')
```

**Descrição**:

- **pd.to_numeric**: Converte a coluna `CD_SITUACAO_PLANO` para valores numéricos, transformando valores inválidos em `NaN`.
- **pd.to_datetime**: Converte as colunas de datas para o formato datetime, permitindo operações e filtragens por data.

## 8. Aplicação de Filtros e Operações Lógicas

```python
filtered_df = df.loc[(df['SG_UF'] == 'PB') & (
    df['DE_SITUACAO_PRINCIPAL'] == 'ATIVO COM COMERCIALIZACAO SUSPENSA')]
```

**escrição**:

- **Filtragem**: Filtra o DataFrame para exibir apenas os registros do estado da Paraíba (`PB`) onde a situação do plano é "Ativo com Comercialização Suspensa".

## 9. Criação de Cópia Segura e Remoção de Colunas Vazias

```python
filtered_df = filtered_df.copy()

filtered_df.dropna(axis=1, how='all', inplace=True)
```

**Descrição**:

- **Cópia**: Cria uma cópia completa do DataFrame filtrado para evitar modificações indesejadas na estrutura original.
- **Remoção de Colunas Vazias**: Remove colunas que estão completamente vazias após a filtragem.


## 10. Agregação de Dados

```python
agg_results = filtered_df.agg({
    'ID_ESTABELECIMENTO_SAUDE': 'count',
    'CD_SITUACAO_PLANO': 'mean'
})
```

**Descrição**:

- **Agregação**: Calcula o número de estabelecimentos de saúde e a média dos códigos de situação dos planos no DataFrame filtrado.

## 11. Aplicação de Funções Condicionais e Transformações

```python
filtered_df.loc['URGENCIA_EMERGENCIA'] = filtered_df['LG_URGENCIA_EMERGENCIA'].apply(lambda x: 'SIM' if x == '1' else 'NÃO')

filtered_df.loc['CD_SITUACAO_PLANO'] = pd.to_numeric(filtered_df['CD_SITUACAO_PLANO'], errors='coerce')

filtered_df.loc['ANO_VINCULO_INICIO'] = pd.to_datetime(filtered_df['DT_VINCULO_INICIO'], errors='coerce').dt.year

filtered_df.loc['NO_RAZAO'] = filtered_df['NO_RAZAO'].str.upper()
```

**Descrição**:

- **Função Condicional**: Transforma a coluna `LG_URGENCIA_EMERGENCIA` em 'SIM' ou 'NÃO', dependendo do valor ('1' ou outro).
- **Conversão Numérica**: Garante que `CD_SITUACAO_PLANO` está em formato numérico para cálculos.
- **Extração de Ano**: Extrai o ano de início do vínculo da data em `DT_VINCULO_INICIO`.
- **Transformação de String**: Converte os valores da coluna `NO_RAZAO` para maiúsculas.

## 12. Remoção Final de Colunas Vazias e Salvamento do Resultado

```python
filtered_df = filtered_df.dropna(axis=1, how='all')

print(filtered_df.head())

filtered_df.to_csv('resultados.csv', index=False)
```

**Descrição**:

- **Remoção Final**: Exclui colunas que possam ter ficado vazias após todas as operações.
- **Exibição dos Resultados**: Exibe as primeiras linhas do DataFrame final para verificação.
- **Salvamento do CSV**: Salva o DataFrame resultante em um arquivo CSV chamado `resultados.csv`.