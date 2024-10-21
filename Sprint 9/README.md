
Nesta sprint, foi possível aprender e praticar diversas habilidades relacionadas ao tratamento e processamento de dados em grandes volumes, utilizando ferramentas e tecnologias de ponta. Os principais aprendizados foram:

1. **Integração de PySpark com AWS Glue**:
    
    - Continuamos a utilizar o **AWS Glue** para executar jobs que processam dados em escala. Através do **PySpark**, realizamos transformações complexas nos dados, como a leitura de arquivos Parquet e o tratamento de colunas numéricas e textuais.
2. **Manipulação e Tratamento de Dados**:
    
    - Foi aplicado o tratamento de colunas que estavam em formatos inadequados, como valores numéricos em notação científica, e conversão de tipos de dados (`budget` e `revenue`).
    - Também foi trabalhada a limpeza de dados, como a eliminação de duplicatas e a conversão de strings para tipos adequados (datas e números).
3. **Modelagem Dimensional**:
    
    - A estruturação dos dados no modelo **dimensional** foi implementada. Criamos tabelas de dimensão (atores, gênero, data, produtora) e a tabela fato com os principais dados dos filmes. Esse tipo de modelagem facilita consultas otimizadas para análises em dashboards e ferramentas de BI.
4. **Criação de Tabelas de Dimensão e Fato**:
    
    - A partir dos dados tratados, foram criadas tabelas separadas para facilitar a análise: tabelas de dimensão com informações específicas (atores, gêneros, etc.) e a tabela fato centralizando métricas de interesse para os filmes.
5. **Pipeline de Dados no S3**:
    
    - Um fluxo de processamento completo foi implementado, desde a leitura de dados da camada **Trusted** até a gravação dos dados processados na camada **Refined** do data lake S3.
6. **Ferramentas para Modelagem e Visualização**:
    
    - Discutimos o uso de ferramentas de modelagem, como o **BrModelo**, para representar graficamente a estrutura do banco de dados e facilitar o entendimento da relação entre as tabelas.

### Conclusão:

Essa sprint proporcionou uma visão completa do ciclo de vida dos dados: desde o **tratamento e limpeza** até a **modelagem** e **armazenamento** adequado, preparando-os para análises futuras.