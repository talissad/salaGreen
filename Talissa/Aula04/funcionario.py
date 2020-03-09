from Talissa.Aula04.Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, numero_registro: int, cargo: str, nome, sobrenome, idade):
        self.__numero_registro = numero_registro
        self.__cargo = cargo
        super().__init__(nome, sobrenome, idade)

    def set_numero_registro(self, registro) -> None:
        self.__numero_registro = registro

    def set_cargo(self, cargo) -> None:
        self.__cargo = cargo

    def get_numero_registro(self) -> int:
        return self.__numero_registro

    def get_cargo(self) -> str:
        return self.__cargo


f = Funcionario(28681681, 'programadora', 'Talissa', 'Dahlke', 22)

print(f.get_cargo())
