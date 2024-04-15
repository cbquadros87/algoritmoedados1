from abc import ABC, abstractmethod

class ContaBancaria(ABC):

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def depositar(self):
        pass