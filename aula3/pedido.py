from pessoa import Pessoa
from cidade import Cidade
from produto import Produto
from categoria import Categoria

class Pedido:

    id = 1
    def __init__(self, end):
        self.end = end
        self.produtos = []
        self.cliente = Pessoa("Carlos")
        self.id = Pedido.id
        Pedido.id += 1

    def add_produto(self, produto):
        self.produtos.append(produto)

    def __str__(self):
        texto = "Endereço do pedido: " + self.end + "\n"
        texto += "ID pedido: " + str(self.id) + "\n"
        texto += "Cliente: " + self.cliente.nome + "\n"
        texto += "Produtos:\n"
        if len(self.produtos) == 0:
            texto += "Não há produtos no pedido."
        else:
            for p in self.produtos:
                texto += " - " + p.nome + " - " + str(p.categoria) + "\n"
        return texto
        