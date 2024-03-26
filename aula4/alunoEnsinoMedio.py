from aluno import Aluno

class AlunoEnsinoMedio(Aluno):

    def __init__(self, codigo, nome, matricula, ano):
        super().__init__(codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print(f"Nome: {self.nome} \nCódigo: {self.codigo} \nMatrícula: {self.matricula} \nAno: {self.ano}")



