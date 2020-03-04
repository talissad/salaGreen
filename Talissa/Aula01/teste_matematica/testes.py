from Talissa.Aula01.teste_matematica.Exercicio03 import Circulo, Quadrado, Retangulo

c = Circulo('Vermelho', 1.2, 'Borracha')
q = Quadrado(14)
r = Retangulo(12, 10)

print('Teste get - Circulo')
assert c.get_cor() == c._Circulo__cor, 'Erro no get cor'
assert c._Circulo__raio == c.get_raio(), 'Erro no get raio'
assert c._Circulo__material == c.get_material(), 'Erro no get material'

print('Teste get - Quadrado')
assert q._Quadrado__tamanho_lado == q.get_valor(), 'Erro no get Tamanho lado'

print('Teste get - Retangulo')
assert r.get_comprimento() == r._Retangulo__comprimento, 'Erro no get Comprimento'
assert r.get_largura() == r._Retangulo__largura, 'Erro no get Largura'

print('Teste set - Circulo')
cores = ['Azul', 'Amarelo', 'Verde', 'Roxo', 1]
numeros = [2.1, 5, 9.8, 9.12, 50]

for i in cores:
    assert c.set_cor(i) == c.get_cor(), f'A cor deveria ser {i}, mas está {c.get_cor()}'
for n in numeros:
    assert c.set_raio(n) == c.get_raio


# print('Teste Calculo - Circulo')
# assert c.calcular_area():.2f == 4.52
