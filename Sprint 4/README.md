### Acesse aqui:

[Certificados](./Certificados/)
[Desafio](./Desafio/)
[Evidências](./Evidencias/)
[Exercícios](./Exercicios/)



## Resumo sobre o que foi aprendido na Sprint 4

### Docker

- **Dockerfile**:
  - Define como construir uma imagem Docker.
  - Especifica imagem base, diretório de trabalho, arquivos a copiar, e o comando a executar.

- **Construção de Imagens**:
  - `docker build -t nome-da-imagem .` constrói a imagem baseada no Dockerfile.

- **Execução de Containers**:
  - `docker run -d --name meu-container minha-imagem` inicia o container em segundo plano.
  - `docker run -it` permite interação direta com o container.
  - Variáveis de ambiente (`-e`) podem definir qual script executar.

- **Gerenciamento de Containers**:
  - `docker stop` para o container, `docker start` reinicia.
  - `docker exec` executa comandos adicionais em containers ativos.
  - `docker logs` acessa a saída gerada pelo container.


### AWS

#### AWS (Amazon Web Services)

- **Conceitos Fundamentais**:
    
    - **Modelo de Responsabilidade Compartilhada**: AWS cuida da infraestrutura, e o cliente da segurança dos dados e aplicações.
    - **Regiões e Zonas de Disponibilidade**: Infraestrutura dividida para garantir alta disponibilidade e redundância.
- **Serviços de Computação**:
    
    - **EC2**: Máquinas virtuais personalizáveis.
    - **Fargate**: Execução de contêineres sem servidor.
    - **Lambda**: Execução de código em resposta a eventos sem servidor.
    - **ECS e EKS**: Gerenciamento de contêineres Docker.
- **Casos de Uso**:
    
    - **Microsserviços**: Fargate ideal para isolar e escalar microsserviços.
    - **Processamento em lote**: Fargate e Lambda para tarefas escaláveis.
    - **Migração para a Nuvem**: EC2 e Fargate facilitam a migração de aplicações on-premises.
- **Outros Serviços Importantes**:
    
    - **S3**: Armazenamento de objetos.
    - **RDS**: Bancos de dados relacionais gerenciados.
    - **EBS**: Armazenamento em bloco persistente para EC2.
- **Benefícios da AWS**:
    
    - **Escalabilidade**: Escalabilidade rápida e fácil dos recursos.
    - **Flexibilidade**: Combinação de serviços para soluções personalizadas.
    - **Custo-benefício**: Pagamento por uso para otimizar custos.
    - **Disponibilidade**: Alta disponibilidade através de regiões e zonas de disponibilidade.