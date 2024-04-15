from Veiculo import *

class Carro(Veiculo):

    def __init__(self, modelo, ano, portas):
        super().__init__(modelo, ano)
        self.qtd_portas = portas

    def ligar(self, chaves):
        if chaves == "1234":
            print("Carro ligado.")
        else:
            print("Carro desligado.")