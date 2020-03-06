#Classes são modelos para a criacao de templates de objeto
#Atributos são variaveis na classe
#A classe só pode ter () se for fazer herança
#__init__ é considerado um construtor e nao pode ter return

class Pessoa:
    def __init__(self):
        self.nome = ''
        self.sobrenome = ''
        self.idade = 0
