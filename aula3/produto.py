from categoria import Categoria

class Produto:

    def __init__(self, id=1, nome="Sabão", preco=2.88, qtd=1):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.categoria = Categoria()