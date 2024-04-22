from abc import ABC, abstractmethod

class Computador(ABC):

    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
       info = "Modelo: " + self.modelo + "\n" + "Cor: " + self.cor + "\n" + "Preço: " + self.preco
       return info

    @abstractmethod
    def cadastrar(self):
        pass