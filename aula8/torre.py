torres = []

class Torre:

    id = 1

    def __init__(self):
        self.id = int(Torre.id)
        self.nome = None
        self.endereco = None
        Torre.id += 1
        torres.append(self)

    def cadastrar(self):
        self.nome = input("Defina o nome da torre: ")
        self.endereco = input("Defina o endereço da torre: ")
    
    def __str__(self):
        return f"ID da torre: {self.id}, Nome da torre: {self.nome}, Endereço: {self.endereco}"

    def imprimir(self):
        print(self)
