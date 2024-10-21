### Desafio Sprint 9 (Criando a camada Refined)

Este job em PySpark processa dados em parquet, gerando tabelas de dimensão e fato em formato Parquet para análise posterior, conforme o modelo dimensional estabelecido. O job é executado no AWS Glue e lê dados da camada Trusted do data lake S3, processa-os e grava a saída na camada Refined.

#### Estrutura do Código

1. Inicialização do Glue Context e Sessão Spark
   Inicia o GlueContext, que permite a integração entre Spark e AWS Glue, e configura a sessão Spark:

```python
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
```

2. Configuração dos Caminhos de Entrada e Saída
   Define os caminhos para os arquivos de entrada (camada Trusted) e de saída (camada Refined) no S3:

```python
input_path = 's3://data-lake-santhiago-santos/Trusted/TMDB/parquet/2024/10/14/'
output_base_path = 's3://data-lake-santhiago-santos/Refined/TMDB/parquet/2024/10/14/'

```

3. Leitura dos Dados do Parquet
   Lê os dados do arquivo Parquet localizado na camada Trusted:

```python
df_fatos = spark.read.parquet(input_path)

```

4. Tratamento dos Campos budget e revenue
   Converte os campos budget e revenue de string para o tipo double, garantindo que os dados numéricos estejam no formato correto para cálculos e análises:

```python
df_fatos = df_fatos.withColumn('budget', F.col('budget').cast('double'))
df_fatos = df_fatos.withColumn('revenue', F.col('revenue').cast('double'))

```

5. Criação das Tabelas de Dimensão
   Dimensão Atores (dim_atores): Seleciona e remove duplicatas dos campos relacionados aos atores (ator_id, ator_nome, ator_personagem, ator_popularity):

```python
dim_atores = df_fatos.select('ator_id', 'ator_nome', 'ator_personagem', 'ator_popularity').dropDuplicates()

```

Dimensão Gênero (dim_genero): Explode(Separa) o campo genres (separado por vírgulas) em múltiplas linhas e gera um genero_id único para cada gênero:

```python
dim_genero = df_fatos.select(F.explode(F.split('genres', ',')).alias('genero')).dropDuplicates() \
    .withColumn('genero_id', F.monotonically_increasing_id())

```
Dimensão Produtora (dim_produtora): Explode o campo production_companies em múltiplas linhas e gera um produtora_id único para cada produtora:

```python
dim_produtora = df_fatos.select(F.explode(F.split('production_companies', ',')).alias('produtora')).dropDuplicates() \
    .withColumn('produtora_id', F.monotonically_increasing_id())

```
Dimensão Data (dim_data): Converte o campo release_date para o tipo date, gera uma ID única e extrai partes da data como ano, mês, dia e trimestre:

```python
df_fatos = df_fatos.withColumn('release_date', F.to_date('release_date'))
dim_data = df_fatos.select('release_date').dropDuplicates() \
    .withColumn('data_id', F.monotonically_increasing_id()) \
    .withColumn('ano', F.year('release_date')) \
    .withColumn('mes', F.month('release_date')) \
    .withColumn('dia', F.dayofmonth('release_date')) \
    .withColumn('trimestre', (F.floor((F.month('release_date') - 1) / 3) + 1).cast('int'))

```
6. Criação da Tabela Fato (fato_filmes)
Seleciona e prepara os campos principais que irão compor a tabela fato, associando o filme às métricas de interesse:

```python
fato_filmes = df_fatos.select(
    F.col('id').alias('filme_id'),
    'budget',
    'revenue',
    'popularity',
    'vote_average',
    'vote_count',
    'release_date'
)

```
7. Gravação das Tabelas em Formato Parquet
Salva todas as tabelas criadas no formato Parquet na camada Refined do S3:

```python
dim_atores.write.mode('overwrite').parquet(output_base_path + 'dim_atores/')
dim_genero.write.mode('overwrite').parquet(output_base_path + 'dim_genero/')
dim_produtora.write.mode('overwrite').parquet(output_base_path + 'dim_produtora/')
dim_data.write.mode('overwrite').parquet(output_base_path + 'dim_data/')
fato_filmes.write.mode('overwrite').parquet(output_base_path + 'fato_filmes/')

```

Descrição das Tabelas Criadas
Tabela Fato: fato_filmes
Esta tabela armazena os dados principais dos filmes com os seguintes campos:

- filme_id: ID único do filme.
- budget: Orçamento do filme.
- revenue: Receita gerada pelo filme.
- popularity: Popularidade do filme.
- vote_average: Média de votos recebidos pelo filme.
- vote_count: Número de votos recebidos.
- release_date: Data de lançamento do filme.

- Tabelas Dimensão:
**dim_atores:** Informações sobre os atores principais dos filmes.

- ator_id: ID único do ator.
- ator_nome: Nome do ator.
- ator_personagem: Personagem interpretado.
- ator_popularity: Popularidade do ator.
**dim_genero:** Gêneros dos filmes.

- genero_id: ID único do gênero.
- genero: Nome do gênero.
**dim_produtora:** Informações sobre as produtoras dos filmes.

- produtora_id: ID único da produtora.
- produtora: Nome da produtora.
**dim_data:** Informações sobre as datas de lançamento dos filmes.

- data_id: ID única da data.
- release_date: Data de lançamento.
- ano: Ano de lançamento.
- mes: Mês de lançamento.
- dia: Dia de lançamento.
- trimestre: Trimestre de lançamento.


### Guia para Evidências de execução

- [Modelo dimensional criado](./Desafio/Modelo%20dimensional_page-0001.jpg)
- [Camada refined criada com sucesso após execução](./Desafio/Camada%20Refined%20criada%20com%20sucesso.png)
- [Job utilizado para tratar e levar os dados para Refined executado com sucesso](./Desafio/Job%20executado%20com%20sucesso.png)
- [Print com código do job - parte 1](./Desafio/Job%20utilizado%20-%20pt1.png)
- [Print com código do job - parte 2](./Desafio/job%20utilizado%20-%20pt2.png)
- [Arquivo do job utilizado](./Desafio/refined_filmes_tmdb.json)
- [Crawler que utilizei para ler as tabelas e enviar para o database](./Desafio/Crawler%20para%20camada%20refined.png)