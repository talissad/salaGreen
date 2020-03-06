class Endereco:
    def __init__(self, rua:str, numero:str, cidade:str, estado:str) -> None:
        self.__rua = ''
        self.__numero = ''
        self.__cidade = ''
        self.__estado = ''

        if type(rua) == str:
            self.__rua = rua
        if type(numero) == str:
            self.__numero = numero
        if type(cidade) == str:
            self.__cidade = cidade
        if type(estado) == str:
            self.__estado = estado

    def get_rua(self) -> str:
        return self.__rua

    def set_rua(self, novo_valor) -> None:
        if type(novo_valor) == str:
            self.__rua = novo_valor

    def get_numero(self) -> str:
        return self.__numero

    def set_numero(self, novo_valor) -> None:
        if type(novo_valor) == str:
            self.__numero = novo_valor

    def get_cidade(self) -> str:
        return self.__cidade

    def set_cidade(self, novo_valor) -> None:
        if type(novo_valor) == str:
            self.__cidade = novo_valor

    def get_estado(self) -> str:
        return self.__estado

    def set_estado(self, novo_valor) -> None:
        if type(novo_valor) == str:
            self.__estado = novo_valor

e = Endereco('rua', 'numero', 'cidade', 'estado')

e.set_cidade('Blumenau')
print(e.get_cidade())