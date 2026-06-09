# Testando heranca

from ContaEspecial import ContaEspecial
from ContaClienteExtrato import Conta
from Cliente import Cliente

cliente1 = Cliente("12345678990", "Adrino", "Rua 1")
cliente2 = Cliente("45678155589", "Emile", "Rua 2")
cliente3 = Cliente("45678277789", "Enzo", "Rua 3")

# As tres contas foram iniciadas, as contas comuns com saldo 2000 e a conta especial com saldo 5000 e limite 1000
conta1 = Conta(cliente1, 123, 2000)
conta2 = Conta(cliente2, 456, 2000)
conta3 = ContaEspecial(cliente3, 789, 1000, 2000)

# Impressao do saldo inicial das contas
print(f"Cliente: {cliente1.nome} da conta comum: {conta1.numero} saldo: {conta1.saldo}")
print(f"Cliente: {cliente2.nome} da conta comum: {conta2.numero} saldo: {conta2.saldo}")
print(
    f"Cliente: {cliente3.nome} da conta especial: {conta3.numero} saldo: {conta3.saldo}"
)

# Depositou 500 na conta comum e tentou sacar 3000, mas nao conseguiu por falta de saldo
conta1.depositar(500)


# Mensagem indicando saldo apos deposito
print( f"Cliente: {cliente1.nome} da conta comum: {conta1.numero} possui o saldo: {conta1.saldo}")


conta2.sacar(3000)
# Mensagem indicando que nao foi possivel sacar por falta de saldo
print(f"Cliente: {cliente2.nome} da conta comum: {conta2.numero} nao possui saldo suficiente!")


# depositou 100 e tentou sacar 2000 da conta especial que tem limite
conta3.depositar(100)
print(f"Cliente: {cliente3.nome} da conta especial: {conta3.numero} possui o saldo: {conta3.saldo} e limite: {conta3.limite}")


conta3.sacar(2000)
# Mensagem indicando que o saque foi realizado e o saldo e limite atualizados
print(f"Cliente: {cliente3.nome} da conta especial: {conta3.numero} possui o saldo: {conta3.saldo} e limite: {conta3.limite}")
