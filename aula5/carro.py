from automovel import *

from veiculo import *

class Carro(Automovel):

    def __init__(self, marca, qtdRodas, modelo, potencia, qtdPortas):
      super().__init__(marca, qtdRodas, modelo, potencia)
      self.qtdPortas = qtdPortas

    def __str__(self):
        texto = super().__str__()
        texto += "\n Portas: " + str(self.qtdPortas)
        return texto

    def imprimirInformacoes(self):
        print("Carro: \n", self)
        