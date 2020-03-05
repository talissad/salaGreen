from Talissa.Aula01.teste_matematica.Exercicio03 import Circulo, Quadrado, Retangulo

c = Circulo('Vermelho', 1.2, 'Borracha')
q = Quadrado(14)
r = Retangulo(12, 10)


print('Teste Get')
assert c.get_cor() == 'Vermelho'
assert c.get_cor() == c._Circulo__cor, 'Erro no get cor'
assert c._Circulo__raio == c.get_raio(), 'Erro no get raio'
assert c._Circulo__material == c.get_material(), 'Erro no get material'
assert q._Quadrado__tamanho_lado == q.get_valor(), 'Erro no get Tamanho lado'
assert r.get_comprimento() == r._Retangulo__comprimento, 'Erro no get Comprimento'
assert r.get_largura() == r._Retangulo__largura, 'Erro no get Largura'
print('Teste get concluido\n')


print('Teste set')
cores = ['Azul', 'Amarelo', 'Verde', 'Roxo', 1]
numeros = [2.1, 5, 9.8, 9.12, 50]
materiais = ['Plastico', 'Borracha', 'Ferro']
for cor in cores:
    c.set_cor(cor)
    assert c.get_cor() == cor, f'A cor deveria ser {cor}, mas está {c.get_cor()}'
for n in numeros:
    c.set_raio(n)
    q.set_valor(n)
    r.set_comprimento(n)
    r.set_largura(n)
    assert c.get_raio() == n, f'O raio é de {n}, mas está {c.get_raio()}'
    assert q.get_valor() == n, f'O valor está em {n}, mas deveria ser {q.get_valor()}'
    assert r.get_largura() == n, f'O valor está em {n}, mas deveria ser {r.get_largura()}'
    assert r.get_comprimento() == n, f'O valor está em {n}, mas deveria ser {r.get_comprimento()}'
for m in materiais:
    c.set_material(m)
    assert c.get_material() == m, f'Material set: {m}, material atual: {c.get_material()}'
print('Teste set concluido\n')


print('Teste calculos')
numeros_testes = [1, 2, 3, 5, 6.5, 9.78]

for n1 in numeros_testes:
    c.set_raio(n1)
    assert c.calcular_area() == 3.141592653589793 * n1 ** 2

    q.set_valor(n1)
    assert q.calcular_area() == n1 * n1

    r.set_comprimento(n1)
    r.set_largura(n1)
    assert r.calcular_area() == n1 * n1
print('Teste de calculo concluido')
