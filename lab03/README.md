# A.3 Serviços Web

**Gabriel Medeiros Lopes Carneiro (19103977)**

Implementar um serviço Web usando SOAP ou REST, de acordo com a sua preferência. 
Deve ser implementado um serviço de uma calculadora, com operações de soma, subtração, multiplicação e divisão. 
Os parâmetros podem ser números inteiros ou reais, ficando a decisão ao seu critério.
Além disso, você pode escolher a linguagem de programação, mas note que seria interessante (mas não obrigatório) explorar linguagens diversas na implementação de diferentes clientes (ex. um cliente em Java outro em Python).

Obs.: Se você usar uma IDE para desenvolvimento, ainda assim procure configurar um servidor Web e disponibilizar o seu serviço para execução fora da IDE.
Por exemplo, o serviço estaria disponível em uma URL como “localhost/seu_servico/calculadora.wsdl”.
Você pode revisar a aula sobre Web e o uso do servidor Web Apache como referência.

## Dependências

```shell
pip install Flask
```

## Uso

Para rodar o servidor use

```shell
python3 server.py
```

Para acessar a calculadora basta rodar o cliente com

```shell
python3 client.py
```

e digitar o cálculo a ser resolvido.

O cálculo deve ser fornecido de uma só vez e com espaço entre números e operador (num1 operador num2). Os números podem ser inteiros ou reais.

**Exemplos Válidos**

- 4 / 2
- 1.2 * 3

**Exemplos Inválidos**

- 4/ 2
- 4 /2

### Operações disponíveis

São suportadas todas as funções que usem dois operandos do python, as quais são acessadas via um dicionário com a _string_ do operando dado, como segue:

```python
op_to_func: Dict[str, Callable] = {
    '+': add,
    '-': sub,
    '*': mul,
    '**': pow,
    '/': truediv,
    '//': floordiv,
    '%': mod,
    '^': xor,
    '>>': rshift,
    '<<': lshift,
    'and': and_,
    '|': or_,
}
```

### Acesso via URL

Também é possível acessar a calculador via url após rodar o servidor.

**Exemplo**

http://localhost:5000/calculator?first_operand=4&op=/&second_operand=2

Aqui está sendo realizado o cálculo de 4 / 2. 
Caso queira outros valores ou outra operação, basta trocar a _string_ logo após o `=` de acordo com o necessário.