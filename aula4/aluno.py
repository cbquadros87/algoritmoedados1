class Aluno:
    
    def __init__(self, codigo: int, nome: str, matricula: int):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print(f"Nome: {self.nome} \nCódigo: {self.codigo} \nMatrícula: {self.matricula}")