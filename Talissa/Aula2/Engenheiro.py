from Talissa.Aula2.Pessoa import Pessoa


class Engenheiro(Pessoa):
    def __init__(self, nome, sobrenome, idade, curso, crea):
        super().__init__(nome, sobrenome, idade)
        self.__curso = curso
        self.__crea = crea

    def get_curso(self):
        return self.__curso
    def set_curso(self, novo_valor):
        self.__curso = novo_valor

    def get_crea(self):
        return self.__crea
    def set_crea(self, novo_valor):
        self.__crea = novo_valor

pes = Engenheiro('Talissa', 'Dahlke', 22, 'Eng. Software', '1581578')
print(pes.get_curso())
