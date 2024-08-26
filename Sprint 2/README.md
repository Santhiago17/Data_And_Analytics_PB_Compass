### SQL

Durante a Sprint, tivemos a oportunidade de aprender diversos conceitos fundamentais de Engenharia de Dados, com foco na manipulação e consulta de bancos de dados SQL. Abaixo, destacamos alguns dos principais conceitos que absorvemos:

#### 1. **Filtragem de Dados com `WHERE`**

- Aprendemos a usar a cláusula `WHERE` para filtrar registros com base em condições específicas, como o status de vendas (`status = 'Concluído'`) ou registros deletados (`deletado = 1`).

#### 2. **Junções de Tabelas (`JOIN`)**

- Estudamos como combinar dados de várias tabelas relacionadas utilizando diferentes tipos de junções, como `INNER JOIN` e `LEFT JOIN`, baseando-se em chaves estrangeiras.

#### 3. **Agrupamento e Agregação de Dados (`GROUP BY` e Funções Agregadas)**

- Praticamos o agrupamento de registros com `GROUP BY` e a aplicação de funções agregadas (`SUM`, `AVG`, `COUNT`) para calcular totais, médias e contagens. Por exemplo, utilizamos `SUM(quantidade * valor_unitario)` para calcular o valor total das vendas.

#### 4. **Ordenação de Resultados (`ORDER BY`)**

- Aprendemos a ordenar os resultados em ordem crescente (`ASC`) ou decrescente (`DESC`) com base em uma ou mais colunas. Por exemplo, `ORDER BY quantidade_vendas ASC` para ordenar as vendas de forma crescente.

#### 5. **Limitação de Resultados (`LIMIT`)**

- Exploramos como restringir o número de registros retornados com `LIMIT`. Por exemplo, `LIMIT 10` para retornar os 10 produtos menos vendidos.

#### 6. **Subconsultas e CTEs (`WITH`)**

- Utilizamos subconsultas e Common Table Expressions (CTEs) para criar consultas intermediárias e simplificar consultas complexas. Por exemplo, identificamos o vendedor com menor valor total de vendas usando uma CTE.

#### 7. **Funções de Formatação e Arredondamento**

- Aprendemos a aplicar funções como `ROUND` para arredondar valores numéricos a um número específico de casas decimais. Um exemplo é `ROUND(AVG(quantidade), 4)` para arredondar a quantidade média vendida.

#### 8. **Filtragem por Intervalos de Data**

- Utilizamos a cláusula `BETWEEN` para filtrar registros dentro de um intervalo de datas. Um exemplo seria `data_venda BETWEEN '2014-02-03' AND '2018-02-02'`.

#### 9. **Cálculo de Métricas de Negócio**

- Estudamos o cálculo de métricas como comissão de vendedores e gasto total de clientes com base em regras de negócio. Por exemplo, calculamos a comissão com `SUM(quantidade * valor_unitario) * perccomissao / 100`.

#### 10. **Identificação e Exclusão de Registros**

- Aprendemos a identificar e excluir registros com condições específicas, como vendas deletadas. Um exemplo é `WHERE deletado = 1`.

Esses conceitos são essenciais para trabalhar de forma eficiente com bancos de dados relacionais, permitindo a extração, transformação e análise de dados de maneira eficaz. A prática contínua desses conceitos prepara nós, os bolsistas, para enfrentar desafios reais na engenharia de dados e análise de negócios.