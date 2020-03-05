import math


class Circulo:
    def __init__(self, cor, raio, material):
        self.__cor = cor
        self.__raio = raio
        self.__material = material

    def set_cor(self, cor):
        self.__cor = cor

    def set_raio(self, raio):
        self.__raio = raio

    def set_material(self, material):
        self.__material = material

    def get_cor(self):
        return self.__cor

    def get_raio(self):
        return self.__raio

    def get_material(self):
        return self.__material

    def calcular_area(self):
        return math.pi * self.__raio ** 2


class Quadrado:
    def __init__(self, tamanho_lado):
        self.__tamanho_lado = tamanho_lado

    def set_valor(self, n1):
        self.__tamanho_lado = n1

    def get_valor(self):
        return self.__tamanho_lado

    def calcular_area(self):
        return self.__tamanho_lado * self.__tamanho_lado


class Retangulo:
    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura

    def set_comprimento(self, n1):
        self.__comprimento = n1

    def set_largura(self, n2):
        self.__largura = n2

    def get_comprimento(self):
        return self.__comprimento

    def get_largura(self):
        return self.__largura

    def calcular_area(self):
        return self.__comprimento * self.__largura
