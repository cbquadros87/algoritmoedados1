from Computador import Computador

class Desktop(Computador):

    def __init__(self, modelo, cor, preco, potencial):
        super().__init__(modelo, cor, preco)
        self._potencialDaFonte = potencial

    def __str__(self) -> str:
        info = "Modelo: " + self.modelo + "\n" + "Cor: " + self.cor + "\n" + "Preço: " + str(self.preco) + "\n" + "Potencial da fonte: " + str(self._potencialDaFonte)
        return info

    def getInformacoes(self):
        return self.modelo, self.cor, self.preco, self._potencialDaFonte

    def cadastrar(self):
        info = self.getInformacoes
        print("O Desktop foi cadastrado com sucesso.")
 