### Guia sobre cada etapa e organização das evidências do desafio referente a esta Sprint

Perguntas a serem respondidas com o desafio final:

Houve uma alteração nas perguntas a serem respondidas no desafio final e agora serão estas abaixo:

1. Quais são os 5 filmes com maior faturamento por década?
2. Quais são os filmes de maior popularidade no século XXI (2000-2022)?

### Sumário para identificação de cada arquivo e sua função
- [Função lambda utilizada para fazer a requisição dos dados de séries](./lambda_function.py)
- [Arquivo referente a validação das chaves da API TMDB](./script_autenticacao_tmdb.py)
- [Arquivo com script para identificar todos os ID's e assim pegar o número dos gêneros Romance/Drama](./scritp_genero_id.py)
- [Arquivo python com código utilizado para requisição dos dados e gravação no S3](./script_lambda_tmdb.py)



### Descrição do Código para Coleta de Dados de Filmes e Séries do TMDB e Armazenamento no S3

O código implementa um processo automatizado para coletar informações de filmes e séries dos gêneros Romance e Drama da API do The Movie Database (TMDB), e então armazená-las no Amazon S3. Este processo foi desenvolvido em Python e pode ser utilizado em um ambiente AWS Lambda. Abaixo, está uma explicação detalhada de cada parte do código.

### Dependências e Bibliotecas Utilizadas

1. requests: Utilizada para fazer as requisições HTTP à API do TMDB.
2. json: Usada para manipular os dados no formato JSON, tanto ao receber os dados da API quanto para preparar o envio ao S3.
3. boto3: Biblioteca oficial da AWS para interagir com os serviços da nuvem, aqui usada para conectar e salvar arquivos no S3.
4. time: Utilizada para incluir atrasos temporários nas requisições, prevenindo a superação dos limites de requisição da API.
5. botocore.exceptions: Importa exceções relacionadas a falhas nas credenciais AWS, para lidar com erros específicos de autenticação.


### Configuração das credenciais AWS

As credenciais da AWS, como aws_access_key_id, aws_secret_access_key e aws_session_token, são fornecidas diretamente no código para autenticar e conectar ao serviço Amazon S3. Esta configuração permite que o script envie os dados coletados para o bucket S3.

```python
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token = aws_session_token
)
```
O cliente boto3.client('s3') é configurado aqui para permitir o envio de arquivos JSON para o bucket do S3.

### Coletas de filme por gênero

A função buscar_filmes_pelo_genero é responsável por fazer as requisições à API do TMDB. Esta função coleta filmes com base no gênero fornecido (Romance ou Drama) e retorna os dados em formato JSON. Algumas particularidades da implementação incluem:

- URL da API: O endpoint usado é o /discover/movie, que permite buscar filmes filtrando por gêneros, datas de lançamento, entre outros parâmetros.
- Parâmetros da Requisição:
    - with_genres: Define o gênero do filme (Romance ou Drama).
    - sort_by: Ordena os resultados pela data de lançamento em ordem decrescente.
    - release_date.lte: Limita os resultados a filmes lançados antes ou até a data fornecida (2022-12-31).
    - A função faz a requisição, imprime o status da resposta e retorna o conteúdo em JSON.

 A função faz a requisição, imprime o status da resposta e retorna o conteúdo em JSON

 ```python
 def buscar_filmes_pelo_genero(genero_id, page=1, data_maxima="2022-12-31"):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "with_genres": genero_id,
        "sort_by": "release_date.desc",
        "page": page,
        "release_date.lte": data_maxima
    }
    response = requests.get(url, params=params)
    time.sleep(1)  # Delay para evitar o excesso de requisições
    return response.json()

 ```

 ### Salvando os Dados no Amazon S3
A função salva_dados_no_s3 é responsável por salvar os dados coletados da API no bucket S3 da AWS. A estrutura do arquivo JSON gerado é definida e organizada por data no caminho: Raw/TMDB/JSON/2024/09/22/filmes_data_{file_index}.json.

Ela tenta realizar a operação de envio, tratando erros relacionados à ausência ou falha de credenciais.

```python
def salva_dados_no_s3(data, file_index):
    filename = f"filmes_data_{file_index}.json"
    s3_path = f"Raw/TMDB/JSON/2024/09/22/{filename}"
    
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_path,
            Body=json.dumps(data, ensure_ascii=False, indent=4),
            ContentType='application/json'
        )
        print(f"✅ Arquivo salvo com sucesso: {filename}")
    except (NoCredentialsError, PartialCredentialsError):
        print("❌ Erro ao enviar para o S3: Credenciais inválidas ou incompletas.")
    except Exception as e:
        print(f"❌ Erro ao enviar o arquivo para o S3: {e}")

```
### Coleta e Processamento de Dados de Múltiplas Páginas
A função coleta_dados_e_salva orquestra o processo de coleta de dados e salvamento no S3. Ela faz o seguinte:

1. Itera pelas páginas de resultados: A API TMDB retorna os resultados paginados, e essa função percorre todas as páginas até alcançar o limite (total_pages).
2. Filtra os filmes por gênero: Garante que apenas os filmes que contenham ambos os gêneros (Romance e Drama) sejam considerados.
3. Gerencia o tamanho do arquivo: Acumula os dados em um buffer, salvando no S3 se o tamanho dos dados ultrapassar 10MB.
4. Salva dados restantes: Caso ainda haja dados no buffer quando todas as páginas forem percorridas, eles são salvos no S3.

```python
def coleta_dados_e_salva(genero_id, data_maxima="2022-12-31"):
    page = 1
    file_index = 1
    filmes_data = []

    while True:
        try:
            data = buscar_filmes_pelo_genero(genero_id, page, data_maxima)
            total_pages = data.get('total_pages', 1)
            filmes = data.get('results', [])

            filmes_filtrados = [
                filme for filme in filmes
                if set([genero_romance, genero_drama]).intersection(filme.get('genre_ids', []))
                and all(genero in [genero_romance, genero_drama] for genero in filme.get('genre_ids', []))
            ]

            if not filmes_filtrados:
                break

            filmes_data.extend(filmes_filtrados)

            # Verificar tamanho dos dados acumulados e salvar se necessário
            tamanho_atual_dados = len(json.dumps(filmes_data).encode('utf-8')) / (1024 * 1024)
            if tamanho_atual_dados > 10:
                salva_dados_no_s3(filmes_data, file_index)
                file_index += 1
                filmes_data = []

            page += 1

            if page >= total_pages:
                break

        except Exception as e:
            break

    if filmes_data:
        salva_dados_no_s3(filmes_data, file_index)
```

### Resumo do Fluxo
1. Requisição dos dados: O script faz requisições à API do TMDB usando o método /discover/movie, filtrando filmes de gêneros específicos.
2. Filtragem dos filmes: Os dados retornados são filtrados para garantir que pertencem aos gêneros Romance e Drama.
3. Salvamento no S3: Os dados filtrados são acumulados e, ao atingirem um limite de tamanho, são salvos em arquivos JSON no bucket S3.
4. Execução via Lambda: A função lambda_handler é configurada para ser executada no ambiente AWS Lambda, permitindo a automação e o agendamento do processo de coleta de dados.

### Evidências de execuções dos scripts

- [Validação da chave do meu usuário com sucesso](../Desafio/Evidencias/sucesso%20na%20validação%20da%20API.png)
- [Trazendo ID's de cada gênero para poder saber qual utilizar](../Desafio/Evidencias/script%20para%20consulta%20dos%20gêneros.png)
- [Execução do script que coleta os dados dos filmes e grava no S3](../Desafio/Evidencias/coleta%20concluída%20TMDB.png)
- [Arquivo JSON gravado no S3 referente aos filmes](../Desafio/Evidencias/arquivo%20da%20requisição%20TMDB%20salvo%20no%20bucket.png)
- [Arquivo JSON gravado no S3 referente aos series](../Desafio/Evidencias/arquivo%20JSON%20series%20S3.png)
- [Criando arquivo com módulo request para inserir na Layer](../Desafio/Evidencias/criando%20pasta%20com%20módulo%20request%20para%20layer.png)
- [Execução da função lambda que traz os dados das séries com sucesso](../Desafio/Evidencias/execução%20concluida%20lambda-series.png)