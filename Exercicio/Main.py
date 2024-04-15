from contaCorrente import *
from contaPoupanca import*

cc = ContaCorrente("Carlos", "123", 15, 5000)
cc.cadastrar()
cc.depositar(500)

cp = ContaPoupanca("Dalessandro", "45", 1.5, 100000)
cp.cadastrar()
cp.depositar(2000)