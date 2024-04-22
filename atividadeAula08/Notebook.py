from Computador import Computador

class Notebook(Computador):

    def __init__(self, modelo, cor, preco, bateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = bateria

    def __str__(self) -> str:
        info = "Modelo: " + self.modelo + "\n" + "Cor: " + self.cor + "\n" + "Preço: " + str(self.preco) + "\n" + "Tempo de bateria: " + str(self.__tempoDeBateria)
        return info

    def getInformacoes(self):
        return self.modelo, self.cor, self.preco, self.__tempoDeBateria

    def cadastrar(self):
        print("O Notebook foi cadastrado com sucesso.")
    