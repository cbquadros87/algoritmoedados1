class Pessoa:

    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def getNome(self):
        return self.nome

    def getTelefone(self):
        return self.__telefone

    def imprimeNome(self):
        print(self.getNome())

    def __imprimeTelefone(self):
        print(self.getTelefone())
    