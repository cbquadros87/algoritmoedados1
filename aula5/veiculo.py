class Veiculo:

    def __init__(self, marca, qtdRodas, modelo):
        self.id = None
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = 0

    def __str__(self):
        texto = "Marca: " + self.marca + "\n" + "Quantidade de rodas: " + str(self.qtdRodas) + "\n" + "Modelo: " + self.modelo + "\n" + "Velocidade atual: " + str(self.velocidade)
        return texto

    def imprimirInformacoes(self):
        print("Veículo: \n", self)

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -+ valor
