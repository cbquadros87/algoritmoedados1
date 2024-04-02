from veiculo import *

class Bicicleta(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro = False):
        super().__init__(marca, qtdRodas, modelo)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def __str__(self):
        texto = "Marca: " + self.marca + "\n" + "Quantidade de rodas: " + str(self.qtdRodas) + "\n" + "Modelo: " + self.modelo + "\n" + "Velocidade atual: " + str(self.velocidade)
        texto += "\n" + "Número de marchas: " + str(self.numMarchas)
        if self.bagageiro == True:
            texto += "\n" + "Possui bagageiro."
            return texto
        else:
            texto += "\n" + "Não possui bagageiro."
            return texto

    def imprimirInformacoes(self):
        print("Bicicleta: \n", self)

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor