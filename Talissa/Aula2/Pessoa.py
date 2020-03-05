class Endereco:
    def __init__(self, rua, numero, cidade, estado):
        self.__rua = rua
        self.__numero = numero
        self.__cidade = cidade
        self.__estado = estado

    #endereco
    def get_rua(self):
        return self.__rua
    def set_rua(self, novo_valor):
        self.__rua = novo_valor

    def get_numero(self):
        return self.__numero
    def set_numero(self, novo_valor):
        self.__numero = novo_valor

    def get_cidade(self):
        return self.__cidade
    def set_cidade(self, novo_valor):
        self.__cidade = novo_valor

    def get_estado(self):
        return self.__estado
    def set_estado(self, novo_valor):
        self.__estado = novo_valor


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        #self.endereco = Endereco()

    #pessoa
    def get_nome(self):
        return self.__nome
    def set_nome(self, novo_valor):
        self.__nome = novo_valor

    def get_sobrenome(self):
        return self.__sobrenome
    def set_sobrenome(self, novo_valor):
        self.__sobrenome = novo_valor

    def get_idade(self):
        return self.__idade
    def set_idade(self, novo_valor):
        self.__idade = novo_valor


#     def alimentar(self, nome):
#         pass
#     def dormir(self, nome):
#         return print(f'A {nome} precisa dormir!')
#     def beber(self):
#         pass
#     def estudar(self):
#         pass
#     def trabalhar(self):
#         pass
#     def entreterimento(self):
#         pass
#
# talissa = Pessoa()
# talissa.dormir('Talissa')
