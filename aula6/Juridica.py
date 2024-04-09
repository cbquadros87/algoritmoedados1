from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def getCnpj(self):
        return self.__cnpj

    def getInscricaoEstadual(self):
        return self.__inscricaoEstadual

    def getQuantidadeFuncionarios(self):
        return self.quantidadeFuncionarios

    def imprimeCNPJ(self):
        print(self.getCnpj)

    def __emitirNotaFiscal(self):
        print("Nota fiscal emitida. CNPJ: " + self.imprimeCNPJ())
