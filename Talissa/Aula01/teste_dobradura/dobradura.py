# DOBRADURA de Papel
#
# Uma professora de arte pediu um programa para clacular quanto poderia dividir um papel com
# uma quantidade de dobradura.
#
# Ela falou que com uma dobradura, poderia dividir o papel em 2 pedaços e com três dobraduras
# pode-se dividir o papel em 8 pedaços.
#
# Faça uma classe que:
# 1) calcule e retorne a quantidade de divisões do papel por uma quantidade de dobradura.
# 2) A quantidade de dobraduras não pode ser numero negativo e nem aceitar string. Caso seja colocado
#       numero negativo e caracteres a função deve retornar False
#
#
# Atenção!!!
# A estrutura do programa é a seguinte:
# 1) Nome da classe: Dobradura.
# 2) Nome do metodo: get_dobrar(self,numero_dobradura)
#
# Deve ser salvado com o nome do arquivo dobradura.py dentro da pasta teste_dobradura.
# Deve ser executado o arquivo teste_de_dobradura.py e o mesmo deve aparecer a mensagem 'Teste Conculido com Sucesso!'


class Dobradura:
    def __init__(self):
        self.numero_dobradura = 0

    def get_dobrar(self, numero_dobradura):
        if type(numero_dobradura) is str or numero_dobradura < 0:
            return False
        else:
            return 2 ** numero_dobradura













    # def get_dobrar(self, numero_dobradura):
    #     if self.verificar() == False:
    #         return False
    #     else:
    #         contador = 1
    #         for i in range(0, numero_dobradura):
    #             contador = 2 ** numero_dobradura
    #         return contador
    #
    # def verificar(self):
    #     while True:
    #         if type(self.numero_dobradura) is str:
    #             return False
    #         elif self.numero_dobradura < 0:
    #             return False
    #         else:
    #             return True

