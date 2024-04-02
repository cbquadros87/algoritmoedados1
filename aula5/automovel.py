from veiculo import *

class Automovel(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, potencia):
        super().__init__(marca, qtdRodas, modelo)
        self.potenciaDoMotor = potencia

    def __str__(self):
        texto = "Marca: " + self.marca + "\n" + "Quantidade de rodas: " + str(self.qtdRodas) + "\n" + "Modelo: " + self.modelo + "\n" + "Velocidade atual: " + str(self.velocidade) + "\n" + "Potência do motor: " + str(self.potenciaDoMotor)
        return texto

    def imprimirInformacoes(self):
        print("Automóvel: \n", self)