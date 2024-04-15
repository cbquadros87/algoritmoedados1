from contaBancaria import *

class ContaCorrente(ContaBancaria):

    def __init__(self, nome, numero, taxa_servico, saldo):
        super().__init__(nome, numero)
        self.taxa_servico = taxa_servico
        self.saldo = saldo

    def cadastrar(self):
        print(f"Conta corrente de {self.nome} cadastrada com sucesso. Taxa de serviço: {self.taxa_servico}")

    def depositar(self, valor):
        self.saldo += valor
        self.saldo -= self.taxa_servico
        print(f"Depósito de {valor} realizado na conta corrente de {self.nome}. Saldo atual: {self.saldo}")
