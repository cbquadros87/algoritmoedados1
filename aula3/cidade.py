class Cidade:

    def __init__(self, id=0, nome="POA"):
        self.id = id
        self.nome = nome

    def __str__(self):
        return "Cidade: " + self.nome


