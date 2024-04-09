from Pessoa import *

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def getCpf(self):
        return self.__cpf

    def getIdade(self):
        return self.idade

    def getPeso(self):
        return self.peso

    def getAltura(self):
        return self.altura

    def imprimirCPF(self):
        print(self.getCpf())

    def __calculoIMC(self):
        imc = self.peso/(self.altura**2)
        return imc
