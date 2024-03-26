from categoria import Categoria

class Produto:

    def __init__(self, id, nome="Sabão", preco=2.88, qtd=1, categoria=Categoria(id, nome=None)):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.categoria = categoria

    def get_nome(self):
        return self.nome
       