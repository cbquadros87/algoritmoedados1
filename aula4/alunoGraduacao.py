from aluno import Aluno

class AlunoGraduacao(Aluno):

    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print(f"Nome: {self.nome} \nCódigo: {self.codigo} \nMatrícula: {self.matricula} \nSemestre: {self.semestre}")