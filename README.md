# Sistema Basico de Banco

Projeto simples em Python para praticar Programacao Orientada a Objetos usando um sistema bancario como exemplo.

O codigo demonstra conceitos como classes, objetos, heranca, heranca multipla, composicao, metodos, saldo, saque, deposito, transferencia, extrato e conta remunerada.

## Objetivo

O objetivo deste repositorio e simular operacoes basicas de um banco, criando clientes e contas com diferentes comportamentos.

Com ele e possivel estudar:

- Criacao de classes em Python
- Uso de construtores com `__init__`
- Relacionamento entre classes
- Heranca entre contas
- Heranca multipla
- Composicao com extrato
- Deposito, saque e transferencia
- Conta especial com limite
- Conta poupanca com remuneracao

## Estrutura do projeto

```text
Heranca/
|-- Cliente.py
|-- Conta.py
|-- ContaClienteExtrato.py
|-- ContaCompleta.py
|-- ContaEspecial.py
|-- ContaRemuneradaPoupanca.py
|-- Extrato.py
|-- Heranca.py
|-- Poupanca.py
`-- README.md
```

## Arquivos

| Arquivo | Descricao |
| --- | --- |
| `Cliente.py` | Define a classe `Cliente`, com CPF, nome e endereco. |
| `Conta.py` | Define uma conta bancaria simples com deposito, saque, transferencia e consulta de saldo. |
| `ContaClienteExtrato.py` | Versao da classe `Conta` com composicao usando a classe `Extrato`. |
| `Extrato.py` | Armazena e exibe as transacoes realizadas em uma conta. |
| `ContaEspecial.py` | Define uma conta especial que herda de `Conta` e possui limite para saque. |
| `Poupanca.py` | Define uma poupanca com taxa de remuneracao mensal. |
| `ContaRemuneradaPoupanca.py` | Usa heranca multipla com `Conta` e `Poupanca` para criar uma conta remunerada. |
| `Heranca.py` | Arquivo de teste para demonstrar clientes, contas comuns e conta especial. |
| `ContaCompleta.py` | Arquivo de teste para demonstrar conta, poupanca e conta remunerada. |

## Como executar

Abra o terminal dentro da pasta `Heranca`:

```bash
cd Heranca
```

Execute um dos arquivos principais:

```bash
python Heranca.py
```

ou:

```bash
python ContaCompleta.py
```

## Exemplo de uso

O arquivo `Heranca.py` cria clientes e contas, faz deposito, tentativa de saque e saque usando limite em uma conta especial.

O arquivo `ContaCompleta.py` cria uma conta remunerada com base em uma taxa de poupanca e atualiza o saldo com remuneracao.

## Conceitos usados

### Classe `Cliente`

Representa uma pessoa cliente do banco.

### Classe `Conta`

Representa uma conta bancaria comum, com metodos para:

- Depositar dinheiro
- Sacar dinheiro
- Transferir valor para outra conta
- Mostrar saldo

### Classe `ContaEspecial`

Herda de `Conta` e adiciona um limite extra para saque.

### Classe `Poupanca`

Representa uma poupanca com taxa de remuneracao.

### Classe `ContaRemuneradaPoupanca`

Combina comportamentos de `Conta` e `Poupanca`, demonstrando heranca multipla.

### Classe `Extrato`

Armazena as transacoes realizadas, como depositos, saques e transferencias.

## Requisitos

Para executar o projeto, e necessario ter o Python instalado.

Nao ha dependencias externas.

## Autor

Projeto desenvolvido para estudo de Python e Programacao Orientada a Objetos.
