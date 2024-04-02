from automovel import *

class Moto(Automovel):

   def __init__(self, marca, qtdRodas, modelo, potencia, partida):
      super().__init__(marca, qtdRodas, modelo, potencia)
      self.partidaEletrica = partida

   def __str__(self):
        texto = "Marca: " + self.marca + "\n" + "Quantidade de rodas: " + str(self.qtdRodas) + "\n" + "Modelo: " + self.modelo + "\n" + "Velocidade atual: " + str(self.velocidade) + "\n" + "Potência do motor: " + str(self.potenciaDoMotor)
        if self.partidaEletrica == True:
            texto += "\n" + "Partida elétrica: sim."
            return texto
        else:
            texto += "\n" + "Partida elétrica: não."
            return texto

   def imprimirInformacoes(self):
        print("Moto: \n", self)
