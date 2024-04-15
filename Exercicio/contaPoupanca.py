from contaBancaria import *

class ContaPoupanca(ContaBancaria):

    def __init__(self, nome, numero, juros, saldo):
        super().__init__(nome, numero)
        self.juros = juros
        self.saldo = saldo

    def cadastrar(self):
        print(f"Conta poupança de {self.nome} cadastrada com sucesso. Taxa de juros: {self.juros}")

    def depositar(self, valor):
        valor_com_juros = valor * (1 + self.juros)
        self.saldo += valor_com_juros
        print(f"Depósito de {valor} realizado na conta poupança de {self.nome}. Saldo atual: {self.saldo}")
