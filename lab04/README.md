# A.4 - Middleware Orientado a Mensagens

**Gabriel Medeiros Lopes Carneiro (19103977)**

**Paulo Arthur Sens Coelho (20150187)**

Implementar uma aplicação no estilo produtor/consumidor, onde alguns processos postam mensagens em fila(s) e outros processos consomem mensagens da(s) fila(s).
A escolha da aplicação é livre.
Portanto, propor uma aplicação hipotética que se beneficie desse modelo de filas de mensagem faz parte desta atividade.

## Aplicação

A aplicação simula o funcionamento de um escalonador tarefas para CPUs.
A tarefa produzida por `producer.py` será mandada para o consumidor (CPU) que estiver livre.
O “tempo de execução” de cada tarefa é simulado a partir do tamanho da mensagem produzida pelo produtor.

- "aaa" levará 3 segundos.
- "aaaa" levará 4 segundos.

## Dependências

```shell
sudo apt install erlang rabbitmq-server
```

Caso algum dos programas não rode execute o *shell script* (fornecido pela própria RabbitMQ) com:

```shell
bash rabbitmq_installer.sh
```

Você também precisará de uma biblioteca python para usar os serviços, instale-a com: 

```shell
pip install -r requirements.txt
```

## Execução

```shell
python3 producer.py
```
```shell
python3 consumer.py
```
