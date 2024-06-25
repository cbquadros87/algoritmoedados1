from torre import *

class Apartamento:

    idApartamento = 1

    def __init__(self):
        self.id = Apartamento.idApartamento
        self.numero = None
        self.torre = None
        self.vaga = None
        self.proximo = None
        Apartamento.idApartamento += 1

    def cadastrar(self):
        self.numero = input("Informe o número do apartamento: ")
        while True:
            torreId = int(input("Informe o ID da torre: "))
            torreEncontrada = None
            for torre in torres:
                if torre.id == torreId:
                    torreEncontrada = torre
                    break
            if torreEncontrada:
                self.torre = torreEncontrada
                break
            else:
                print("Digite um número válido.")
        if self.id < 11:
            self.vaga = self.id

    def imprimir(self):
        print(self)

    def __str__(self):
        return f"Número: {self.numero}, Torre: {self.torre}, Vaga: {self.vaga}"
