# Java RMI

## Execução

Servidor: `java Server`
Cliente (terminal): `java CLIENT_TERMINAL`
Cliente (interface): `java CLIENT_UI`

## Perguntas

**O acesso ao objeto remoto é sequencial ou concorrente? Você deveria se preocupar com condições de corrida na reserva das cadeiras?**

Ser sequencial ou concorrente vai depender. Caso vários clientes realizem chamada ao objeto no mesmo momento, pode causar uma condição de corrida.

**Imagine que há um grande número de requisições para compras de ingressos.
Como você poderia aumentar a concorrência ao acesso do objeto remoto?**

O método `synchronized` deve evitar problemas com a condição de corrida.
Se considerarmos ser somente preciso reservar um assento qualquer (sem importar qual) pode-se dividir ingressos em grupos, para permitir acesso simultâneo a múltiplos objetos e melhorar o acesso à compra. 