class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.limite_saque = 500.0
        self.saques_diarios = 3
        self.saques_realizados = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")
    
    def sacar(self, valor):
        if self.saques_realizados >= self.saques_diarios:
            print("Limite de saques diários atingido!")
        elif valor > self.limite_saque:
            print(f"O valor máximo para saque é R$ {self.limite_saque:.2f}")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        elif valor > 0:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido!")
    
    def exibir_extrato(self):
        print("\nExtrato da conta:")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

banco = Banco()

while True:
    print("\nBem-vindo ao Banco!")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor para depósito: "))
        banco.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))
        banco.sacar(valor)
    elif opcao == "3":
        banco.exibir_extrato()
    elif opcao == "4":
        print("Obrigado por utilizar o Banco! Até mais.")
        break
    else:
        print("Opção inválida! Tente novamente.")
