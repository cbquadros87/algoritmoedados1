from apartamento import *

class Lista:

    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, apartamento):
        if self.inicio == None:
            self.inicio = apartamento
            self.tamanho = 1
        else:
            auxiliar = self.inicio
            while auxiliar.proximo:
                auxiliar = auxiliar.proximo
            auxiliar.proximo = apartamento
            self.tamanho += 1

    def excluir(self, vaga):
        if self.tamanho == 0:
            print("A lista está vazia.")
        elif self.tamanho == 1:
            if self.inicio.vaga == vaga:
                self.inicio = None
            else:
                print("Não encontrado o apartamento informado!")
        else:
            anterior = self.inicio
            auxiliar = anterior.proximo
            while auxiliar:
                if auxiliar.vaga == vaga:
                    anterior.proximo = auxiliar.proximo
                    self.tamanho -= 1
                else:
                    anterior = auxiliar
                    

            
        
