# Sistema Bancário em Python

Este projeto implementa um sistema bancário simples em Python, permitindo operações de **depósito, saque e extrato**.

## Funcionalidades
- **Depósito**: O usuário pode depositar qualquer valor positivo.
- **Saque**:
  - Limite de **3 saques diários**.
  - Valor máximo de **R$ 500,00 por saque**.
  - O sistema impede saques superiores ao saldo disponível.
- **Extrato**:
  - Exibe todos os depósitos e saques realizados.
  - Mostra o saldo atual da conta.
  - Caso não haja movimentações, exibe a mensagem: *"Não foram realizadas movimentações."*

## Como Executar
1. Certifique-se de ter o **Python** instalado em seu computador.
2. Salve o arquivo do código como `banco.py`.
3. No terminal ou prompt de comando, execute:
   ```sh
   python banco.py
   ```
4. Utilize o menu interativo para realizar operações bancárias.

## Exemplo de Uso
```
Bem-vindo ao Banco!
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair
Escolha uma opção: 1
Digite o valor para depósito: 1000
Depósito de R$ 1000.00 realizado com sucesso!
```

## Tecnologias Utilizadas
- Python 3

Este projeto é uma ótima oportunidade para praticar lógica de programação, controle de fluxo e manipulação de dados em Python.

