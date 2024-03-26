from cidade import Cidade

class Pessoa:

    id = 1

    def __init__(self, nome, idade=18, cid=Cidade(1, "POA")):
        self.nome = nome
        self.idade = idade
        self.cidade = cid
        self.id = Pessoa.id
        Pessoa.id += 1
        print("Pessoa", self.nome, "construída.")

    def get_nome(self):
        return self.nome
        