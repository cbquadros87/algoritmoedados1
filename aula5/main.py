from carro import *
from moto import *
from bicicleta import *
from veiculo import *
from automovel import *

moto = Moto("BMW", 2, "Honda", 20, True)
moto.imprimirInformacoes()

carro = Carro("Toyota", 4, "bmw", 5, 4)
carro.imprimirInformacoes()

bike = Bicicleta("Caloi", 2, "Forte", 2, False)
bike.imprimirInformacoes()

bike.acelerar(50)
bike.imprimirInformacoes()
bike.frear(20)
bike.imprimirInformacoes()