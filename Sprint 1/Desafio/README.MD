## Instruções

Este arquivo trás algumas referências e detalhes sobre os desafios da Sprint 1 que se refere a criação de alguns scripts executáveis no Linux e a criação deste repositório para documentação de toda a jornada do programa de bolsas.


### Desafio Git e Github

Foi criado este repositório seguindo as orientações do desafio, baseando-se nas melhores práticas de commits semânticos e estruturação de diretórios conforme é destacado nas instruções do desafio. Aqui constarão todos os arquivos que serão necessários durante todo o decorrer do programa de bolsas.


### Desafio Linux / Markdown.

[Scripts no formato txt.](./Linux%20e%20Markdown/entrega.txt)

#### Etapas para reexecução do desafio

- Fazer o download do arquivo dados_de_vendas.csv
- Fazer o download do arquivo processamento_de_vendas.sh
- Execute o arquivo processamento_de_vendas.sh
- Após fazer isso todas os diretórios e arquivos solicitados no desafio serão criados. 
- Execute o script processamento_de_vendas.sh pelo menos três vezes atráves do comando "crontab -e" e depois insira os horários desejados para execução.
- Utilize o crontab para automatiza e agendar o script para ser executado conforme o exemplo abaixo:

**Abra o crontab**

```shell
crontab -e
```

**Exemplo de agendamento de execução**

```shell
Ex: 27 15 * * 1-4 /home/user/ecommerce/processamento_de_vendas.sh >> /home/user/ecommerce/processamento_de_vendas.log 2>&1
```
- Após ter executadoo script processamento_de_vendas.sh pelo menos três vezes, execute manualmente o script consolidador_de_processamento_de_vendas.sh para obter o relatório final.


