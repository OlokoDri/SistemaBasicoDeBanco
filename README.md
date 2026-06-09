# 🏦 Sistema Básico de Banco

Projeto desenvolvido em **Python** com o objetivo de praticar os principais conceitos de **Programação Orientada a Objetos (POO)** através da simulação de um sistema bancário.

O sistema implementa funcionalidades como contas bancárias, clientes, extrato de transações, conta especial com limite, conta poupança remunerada e herança múltipla, demonstrando na prática conceitos fundamentais da orientação a objetos.

---

## 📚 Objetivo

Este projeto foi criado para consolidar conhecimentos em Python e Programação Orientada a Objetos, explorando:

* Classes e Objetos
* Encapsulamento
* Herança
* Herança Múltipla
* Composição
* Métodos e Construtores (`__init__`)
* Polimorfismo básico
* Organização de código em múltiplos arquivos

---

## 🚀 Funcionalidades

### 👤 Clientes

* Cadastro de clientes
* Armazenamento de CPF, nome e endereço

### 💰 Contas Bancárias

* Depósito
* Saque
* Consulta de saldo
* Transferência entre contas

### 📄 Extrato

* Registro das movimentações realizadas
* Histórico de transações

### ⭐ Conta Especial

* Limite adicional para saque
* Herança da classe Conta

### 📈 Conta Remunerada

* Aplicação de taxa de rendimento
* Simulação de conta poupança
* Utilização de herança múltipla

---

## 🛠️ Tecnologias Utilizadas

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,git,github,vscode" />
</p>

* Python 3
* Git
* GitHub
* Visual Studio Code

---

## 📂 Estrutura do Projeto

```text
Heranca/
│
├── Cliente.py
├── Conta.py
├── ContaClienteExtrato.py
├── ContaCompleta.py
├── ContaEspecial.py
├── ContaRemuneradaPoupanca.py
├── Extrato.py
├── Heranca.py
├── Poupanca.py
└── README.md
```

---

## 📋 Arquivos do Projeto

| Arquivo                    | Descrição                                      |
| -------------------------- | ---------------------------------------------- |
| Cliente.py                 | Classe responsável pelos dados do cliente      |
| Conta.py                   | Implementa operações básicas da conta bancária |
| ContaClienteExtrato.py     | Conta utilizando composição com Extrato        |
| Extrato.py                 | Registro das movimentações da conta            |
| ContaEspecial.py           | Conta com limite adicional para saque          |
| Poupanca.py                | Implementa taxa de remuneração                 |
| ContaRemuneradaPoupanca.py | Exemplo de herança múltipla                    |
| Heranca.py                 | Demonstração de contas comuns e especiais      |
| ContaCompleta.py           | Demonstração de conta remunerada               |

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/OlokoDri/SistemaBasicoDeBanco.git
```

### 2. Acesse a pasta do projeto

```bash
cd SistemaBasicoDeBanco/Heranca
```

### 3. Execute um dos exemplos

```bash
python Heranca.py
```

ou

```bash
python ContaCompleta.py
```

---

## 🎓 Conceitos de POO Aplicados

### Herança

A classe `ContaEspecial` herda comportamentos da classe `Conta`, adicionando um limite de saque.

### Herança Múltipla

A classe `ContaRemuneradaPoupanca` combina funcionalidades das classes `Conta` e `Poupanca`.

### Composição

A classe `ContaClienteExtrato` utiliza a classe `Extrato` para registrar movimentações financeiras.

### Encapsulamento

Os atributos e métodos são organizados dentro das classes para representar entidades do sistema bancário.

---

## 🔮 Melhorias Futuras

* [ ] Interface gráfica com Tkinter
* [ ] Persistência de dados em arquivos
* [ ] Integração com banco de dados SQLite
* [ ] Sistema de autenticação
* [ ] Cadastro de múltiplos clientes
* [ ] Testes automatizados

---

## 👨‍💻 Autor

**Adriano**

🎓 Estudante de Engenharia de Software

🔗 GitHub: https://github.com/OlokoDri

---

⭐ Se este projeto foi útil para você ou ajudou nos estudos de POO, considere deixar uma estrela no repositório.
