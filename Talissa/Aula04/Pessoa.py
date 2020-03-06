class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.__nome = ''
        self.__sobrenome = ''
        self.__idade = 0

        if type(nome) == str:
            self.__nome = nome
        if type(sobrenome) == str:
            self.__sobrenome = sobrenome
        if self.__verifica_idade(idade):
            self.__nome = nome

    def __verifica_idade(self, idade) -> bool:
        if type(idade) == int and idade > 0:
            return True
        return False

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, novo_valor) -> None:
        if type(novo_valor) == str:
            self.__nome = novo_valor

    def get_sobrenome(self) -> str:
        return self.__sobrenome

    def set_sobrenome(self, novo_valor) -> None:
        if type(novo_valor) == str:
            self.__sobrenome = novo_valor

    def get_idade(self) -> int:
        return self.__idade

    def set_idade(self, novo_valor) -> None:
        if self.__verifica_idade(novo_valor):
            self.__idade = novo_valor


p = Pessoa('', '', 0)

p.set_nome('Talissa')
p.set_idade(1)
print(p.get_nome())

assert p.get_nome() == 'Talissa'