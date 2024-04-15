from Veiculo import *

class Moto(Veiculo):

    def __init__(self, modelo, ano, cilindradas):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas

    def ligar(self, chaves):
        if chaves == "1234":
            print("Moto ligado.")
        else:
            print("Moto desligado.")

    def imprimir(self):
        print("Motocicleta")
        super().imprimir()
        print("Clindradas ", self.cilindradas)