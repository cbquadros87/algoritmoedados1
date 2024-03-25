from cidade import Cidade
from pessoa import Pessoa

c1 = Cidade()
c2 = Cidade(nome = "Caxias")
c3 = Cidade(1, "Farroupilha")
c4 = Cidade(2)
c5 = Cidade(id=3)

print(c1)
print(c2)
c2.nome = "Nova Milano"
print(c2)
print(c3)

p1 = Pessoa("Jagger")
p2 = Pessoa("Richards", 20)
p3 = Pessoa("Wood", 25, c1)
p4 = Pessoa("Wood", cid = c4)
p5 = Pessoa("Duda", idade=28)