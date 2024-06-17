class Livro():

    def __init__(self, nome, autor, paginas):
        self.nome = nome
        self.autor = autor
        self.paginas = paginas
        self.proximo = None

    def __str__(self) -> str:
        return f"Livro: {self.nome}, Autor: {self.autor}, Páginas: {self.paginas}"

class Pilha():

    def __init__(self):
        self.topo = None

    def adicionar(self, livro):
        if self.topo == None:
            self.topo = livro
        else:
            livro.proximo = self.topo
            self.topo = livro
        return self

    def remover(self):
        if self.topo == None:
            print("Pilha vazia.")
        else:
            self.topo = self.topo.proximo

    def imprimir(self):
        if self.topo == None:
            print("A lista está vazia.")
        else:
            print("Imprimindo a lista:")
            atual = self.topo
            while atual:
                print(atual)
                atual = atual.proximo

livroUm = Livro("The Rule of Two", "Darth Bane", 333)

livroDois = Livro("How to Conquer London", "Tommy Shelby", 1898)

livroTres = Livro("Seu Madruga Boxeador", "Seu Barriga", 40)

pilha = Pilha()

pilha.imprimir()
pilha.adicionar(livroDois)
pilha.adicionar(livroUm)
pilha.adicionar(livroTres)
pilha.imprimir()
pilha.remover()
pilha.imprimir()
pilha.adicionar(livroTres)
pilha.imprimir()