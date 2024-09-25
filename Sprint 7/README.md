### Resumo do que foi aprendido na Sprint 7

### Integração com APIs e Tratamento de Dados
A experiência de integração com a API do TMDB trouxe importantes aprendizados sobre o funcionamento de APIs RESTful e como lidar com diferentes cenários ao consumir dados de uma fonte externa. Pude aprimorar a habilidade de fazer requisições HTTP, utilizando parâmetros e cabeçalhos adequados, e também a importância de tratar as respostas da API de forma eficiente, seja filtrando os dados de interesse ou lidando com erros e exceções.

Pontos importantes aprendidos:
A necessidade de lidar com limites de requisição (através de mecanismos como time.sleep).
Como paginar resultados e consolidar dados provenientes de várias requisições.
Filtragem de dados para garantir a precisão da informação coletada.

### Armazenamento de Dados no S3 com Boto3
O uso da biblioteca Boto3 para interagir com o Amazon S3 foi crucial nesta sprint. Isso trouxe uma compreensão mais profunda sobre como trabalhar com serviços de armazenamento na nuvem. Foi possível perceber a flexibilidade do S3 para armazenar grandes volumes de dados em diferentes formatos e a facilidade com que podemos criar rotinas automatizadas para manipulação e upload de arquivos JSON.

Aspectos aprendidos:
Como configurar credenciais AWS no código para permitir a comunicação segura com o S3.
Práticas de gerenciamento de dados, como dividir grandes volumes de dados em múltiplos arquivos para facilitar o processamento e armazenamento.
Uso de tratamentos de exceção para assegurar que os dados sejam salvos corretamente, mesmo em cenários de falha de credenciais ou falhas de conexão.
### AWS Lambda e Automação Serverless

Essa sprint envolveu a execução do código em um ambiente AWS Lambda, o que me proporcionou um aprendizado mais prático sobre computação serverless. Entender como a Lambda permite a execução de funções sob demanda, sem a necessidade de manter servidores, foi um avanço em termos de eficiência e escalabilidade.

Principais lições:
A importância de otimizar funções Lambda para que sejam eficientes, especialmente em termos de tempo de execução e consumo de recursos.
Como utilizar eventos para disparar funções Lambda automaticamente, o que pode ser explorado para coleta periódica de dados ou outros processos automatizados.
Limitações de armazenamento e tempo de execução da AWS Lambda, o que reforça a importância de dividir tarefas e gerenciar grandes volumes de dados de forma eficiente.

### Conceitos de Spark e PySpark

Paralelamente ao desenvolvimento da solução com Lambda e S3, tive a oportunidade de estudar e aprofundar os conhecimentos em Apache Spark e PySpark, que são ferramentas amplamente utilizadas para processar grandes volumes de dados de maneira distribuída.

Apache Spark: Entendi que é uma plataforma poderosa para processamento distribuído de dados, que pode ser utilizada em grandes clusters para processar datasets massivos de forma rápida e eficiente. Seus principais componentes incluem:

RDDs (Resilient Distributed Datasets): Estruturas que permitem a distribuição de dados em diferentes nós de um cluster, garantindo a tolerância a falhas e a execução paralela de tarefas.
DataFrames: Estruturas de dados otimizadas que permitem operações de manipulação de dados com uma interface similar ao Pandas, mas distribuída.
PySpark: Uma interface Python para o Spark que facilita o processamento de dados massivos com uma linguagem de programação familiar. Além de reforçar conceitos de processamento distribuído, foi possível aprender:

Transformações e Ações: Spark divide o processamento em transformações (operações "preguiçosas", que não executam imediatamente) e ações (que disparam a execução das transformações). Isso permite otimizar o pipeline de dados.
Integração com outras ferramentas: PySpark pode ser integrado a uma variedade de fontes de dados, como S3 e bancos de dados SQL, permitindo processar e transformar dados diretamente em um cluster distribuído.

### Conclusão

Esta sprint trouxe um avanço significativo em vários aspectos. Pude não apenas aprimorar habilidades técnicas relacionadas ao consumo de APIs e manipulação de dados em ambientes na nuvem, mas também entender melhor como organizar grandes volumes de dados e automatizar processos com Lambda e S3. Além disso, o estudo de Spark/PySpark abriu portas para o entendimento de como grandes empresas lidam com processamento de dados em escala, preparando o terreno para trabalhar com pipelines de dados complexos no futuro.

Esses aprendizados fortalecem a visão de como implementar soluções de ponta a ponta, seja em uma arquitetura serverless ou em um ambiente de processamento distribuído.