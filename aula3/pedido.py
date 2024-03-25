from pessoa import Pessoa
from cidade import Cidade
from produto import Produto

class Pedido:

    def __init__(self, id, end):
        self.id = id
        self.end = end
        self.produto = []
        self.cliente = Pessoa("Carlos")

    def add_produto(self, produto):
        self.produto.append(produto)

    def __str__(self):
        return f"Número do pedido: {self.id}, Endereço: {self.end}, Produtos pedidos: {self.produto}, Cliente: {self.cliente}"

    
produto1 = Produto()
p1 = Pedido(2, "91330190")
p1.add_produto(produto1)

print(p1)