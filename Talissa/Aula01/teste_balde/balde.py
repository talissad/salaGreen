# O volume do balde deve ser o atributo privado __balde para o volume total do balde
# O volume do balde deve ser o atributo privado __balde_atual para o volume atual do balde
# Crie o metodo get_volume_balde() que mostre o volume do balde.
# crie o metodo set_volume_balde(self,volume_balde) que receba como parametro um número inteiro,
# positivo, dentro de 10 a 50.

# Crie o metodo enchendo_balde(self,volume_agua) que deve receber um número inteiro,
# positivo e retornar 'Vazio' se o balde não estiver cheio e True se o balde estiver
# cheio e False se o balde estiver tranbordando. Se o metodo receber valores inválidos,
# deverá retornar "ValorError"

# crie o metodo para sorteio_(). Este metodo deve sortear,
# usando a função randint(), o volume do balde é um número inteiro que vai de 10 a 50,
# para qualquer valor fora disso deverá retornar False.

# O nome da classe deve ser Balde
#
# Salve esta classe na pasta teste_balde com o nome balde.py
# Teste esta classe usando executando o arquivo teste_do_balde.py
#
# Em outro arquivo, importe esta classe e crie um jogo em que o jogoador
#  deva acertar o volume do balde. Caso o volume exceda o jogo termina avisando
# que transbordou água do balde.


from random import randint


class Balde:
    def __init__(self):
        self.__balde = 0
        self.__balde_atual = 0

    def get_volume_balde(self):
        return self.__balde

    def set_volume_balde(self, volume_balde):
        if type(volume_balde) is int and volume_balde > 0:
            if 10 <= int(volume_balde) and 50 >= volume_balde:
                self.__balde_atual = volume_balde
                self.__balde += self.__balde_atual
            else:
                self.enchendo_balde(volume_balde)
        elif type(volume_balde) is str or volume_balde < 0:
            return False
        else:
            return False

    def enchendo_balde(self, volume_agua):
        if type(volume_agua) is int:
            if volume_agua < 0:
                return 'ValorError'
            elif volume_agua > 50:
                return False
            elif 0 == volume_agua:
                return print('Vazio!')
            elif volume_agua == 50:
                return True
            else:
                return 'ValorError'
        else:
            return False, print('ValorError')


    def sorteio(self):
        self.__balde = randint(10, 50)
