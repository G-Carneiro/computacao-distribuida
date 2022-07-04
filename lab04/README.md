# A.4 - Middleware Orientado a Mensagens

Implementar uma aplicação no estilo produtor/consumidor, onde alguns processos postam mensagens em fila(s) e outros processos consomem mensagens da(s) fila(s).
A escolha da aplicação é livre.
Portanto, propor uma aplicação hipotética que se beneficie desse modelo de filas de mensagem faz parte desta atividade.

## Dependências

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

## Aplicação

A aplicação simula o funcionamento de um escalonador tarefas para CPUs.
A tarefa produzida por `producer.py` será mandada para o consumidor (CPU) que estiver livre.
O “tempo de execução” de cada tarefa é simulado a partir do tamanho da mensagem produzida pelo produtor.

- "aaa" levará 3 segundos.
- "aaaa" levará 4 segundos.
