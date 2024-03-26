from pessoa import Pessoa
from cidade import Cidade
from produto import Produto
from categoria import Categoria
from pedido import Pedido


categoria1 = Categoria(1, "Limpeza")
p1 = Produto(1, "Sabão", 3.01, 1, categoria1)
pedido1 = Pedido(end="91330190")
pedido1.add_produto(p1)

print(pedido1)