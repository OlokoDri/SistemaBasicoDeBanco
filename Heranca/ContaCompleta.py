from Cliente import Cliente
from Conta  import Conta
from Poupanca import Poupanca
from ContaRemuneradaPoupanca import ContaRemuneradaPoupanca


cliente1 = Cliente("123", "Adriano", "Rua Z")
cliente2 = Cliente("456", "Emile", "Rua A")

conta1 = Conta([cliente1, cliente2], 1, 2000)
contapoupanca1 = Poupanca(0.1)
contaremunerada1 = ContaRemuneradaPoupanca(0.1, [cliente1], 5, 1000)

contaremunerada1.remuneraConta()
contaremunerada1.gerarSaldo()