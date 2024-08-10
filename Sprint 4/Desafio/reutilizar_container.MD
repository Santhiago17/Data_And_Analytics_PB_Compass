### É Possível Reutilizar um Container?

Sim, é possível reutilizar um container Docker que já foi criado e está parado. Ao invés de criar um novo container, você pode simplesmente reiniciar o container existente e continuar utilizando-o. Abaixo estão as etapas e os comandos necessários para reutilizar um container Docker.

#### Passo 1: Verificar o Status do Container

Primeiro, você deve verificar se o container está parado ou em execução. Use o seguinte comando para listar todos os containers, incluindo os parados:

```
docker ps -a
```
Procure pelo nome do container que você deseja reutilizar (por exemplo, `mascarar-container`). Se o container estiver listado com o status `Exited`, isso significa que ele está parado.

#### Passo 2: Reiniciar o Container Parado

Se o container estiver parado, você pode reiniciá-lo com o comando:

```
docker start mascarar-container
```

Este comando inicia o container sem criar um novo. Ele retomará a execução do container a partir do ponto onde parou.

#### Passo 3: Acessar o Container Interativamente

Se você precisar acessar o container para executar comandos ou interagir com ele, utilize:

```
docker exec -it mascarar-container /bin/sh
```

#### Passo 4: Verificar Logs (Opcional)

Para revisar o que aconteceu no container até o momento, você pode verificar os logs com:

```
docker logs mascarar-container
```
### Conclusão

Reutilizar um container Docker é uma prática comum e eficiente quando você deseja manter o estado de um ambiente ou continuar um processo sem a necessidade de configurar tudo novamente. Com os comandos descritos acima, você pode facilmente reiniciar e interagir com containers existentes, aproveitando ao máximo o Docker em seu fluxo de trabalho.