### Resumo da Sprint

Nesta sprint, foquei no processamento e transformação de dados usando **AWS Glue** e **PySpark**, realizando operações de ETL em arquivos JSON e CSV. Trabalhei desde a leitura e filtragem dos dados até a escrita final no formato **Parquet**, com atenção ao tratamento de dados ausentes e à conversão de tipos de colunas.

---

### Principais Aprendizados:

1. **Manipulação de Arquivos JSON e CSV**:
    
    - Li e transformei arquivos JSON e CSV usando PySpark, garantindo que os dados fossem filtrados, limpos e preparados para análise.
    - Ajustei colunas e apliquei regras de limpeza, como remoção de dados irrelevantes, preenchimento de valores nulos e conversão de tipos, principalmente em colunas de data e números.
2. **Tratamento de Dados Ausentes**:
    
    - Utilizei técnicas de preenchimento de valores nulos com dados padrão para evitar problemas em etapas posteriores.
    - Apliquei filtros condicionais para garantir a integridade dos dados, removendo registros incompletos ou inconsistentes.
3. **Conversão de Tipos e Limpeza de Colunas**:
    
    - Converto datas e números de forma correta, garantindo que as colunas estejam no formato adequado para consultas e análises.
    - Excluí colunas desnecessárias para otimizar o armazenamento e processamento dos dados.
4. **Escrita de Dados em Parquet**:
    
    - Armazenei os dados tratados no formato **Parquet**, aproveitando sua eficiência para consultas analíticas e compressão de dados.
5. **Automação com Glue e PySpark**:
    
    - Automatizei o processo de ETL no Glue, capturando parâmetros do job e integrando com o S3, o que facilita a execução e manutenção do pipeline de dados.

---

A sprint reforçou meu entendimento sobre processamento de grandes volumes de dados em ambientes de nuvem, aprimorando minha capacidade de manipular e transformar dados de maneira eficiente e escalável.