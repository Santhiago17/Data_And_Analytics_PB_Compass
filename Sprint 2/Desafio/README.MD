#### Pequeno resumo sobre o  passo a passo da resolução do desafio de SQL proposto na Sprint 2.

### Modelagem Relacional

###### Normalização da tabela

A tabela tb_locacao foi subdividida em 5 novas tabelas que são: Carro, Cliente, Locação, Combustível e Vendedor que possuem suas respectivas chaves primárias e estrangeiras.

Após isso foram inseridos os respectivos dados da tabela tb_locacao para as novas tabelas. Na tabela Carro haviam alguns itens duplicados na coluna 'idCarro', então foi necessário realizar um tratamento de dados na hora da inserção.

```sql
WITH CarroCTE AS (
    SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel,
           ROW_NUMBER() OVER (PARTITION BY idCarro ORDER BY idCarro) AS rn
    FROM tb_locacao
)
INSERT INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM CarroCTE
WHERE rn = 1;


```

Após cada inserção em suas respectivas tabelas, foi identificado que todas as regras de normalização F1N,F2N e F3N foram atendidas com sucesso. Então partimos para a criação do desenho do modelo relacional.

Após feito o desenho do modelo relacional, foi dado início a criação do modelo dimensional com as tabelas fato e dimensão.

### Modelagem Dimensional

O modelo dimensional segue o esquema estrela, onde uma tabela de fatos central está conectada a várias tabelas dimensionais. Este tipo de relacionamento é 1 para N, onde um fato está ligado a um produto, mas um produto pode estar ligado a diversos fatos.

#### Dimensões:

A dimensão `Cliente` armazena informações detalhadas sobre os clientes que realizam locações. Isso nos permite analisar as locações por diferentes características dos clientes, como cidade, estado e país.

A dimensão `Carro` armazena informações detalhadas sobre os carros que são locados. Isso permite analisar as locações com base nas características dos carros, como marca, modelo e tipo de combustível.

Embora não seja essencial para todas as análises, a dimensão `Combustivel` armazena detalhes sobre os tipos de combustível usados pelos carros. Isso pode ser útil para análises mais específicas relacionadas ao tipo de combustível.

A dimensão `Vendedor` armazena informações sobre os vendedores responsáveis pelas locações. Isso permite analisar o desempenho dos vendedores e entender melhor as características de vendas.

A tabela de fato `Locacao` armazena os eventos principais de locação de carros. Ela contém referências (chaves estrangeiras) para as dimensões e medidas quantitativas das locações.