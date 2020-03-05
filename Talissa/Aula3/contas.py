def soma(n1, n2) -> int:
    return n1 + n2

def multiplica(n1, n2, n3=1):
    return n1 * n2 * n3

def soma_concaterna(valor1, valor2):
    return valor1 + valor2


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resultado = soma(n1, n2)
print(f'O resultado da soma de {n1} + {n2} é igual a {resultado}\n')


mult1 = int(input('Digite um número: '))
mult2 = int(input('Digite outro número: '))

opcao = input('Gostaria de adicionar mais um número? (S/N)')
if opcao.upper() == 'S':
    mult3 = int(input('Digite outro número: '))
    resultado = multiplica(mult1, mult2, mult3)
    print(f'O resultado da multiplicação de {mult1} * {mult2} * {mult3} é {resultado}\n')
else:
    resultado = multiplica(mult1, mult2)
    print(f'O resultado da multiplicação de {mult1} * {mult2} é {resultado}\n')


valor1 = input('Digite algo: ')
valor2 = input('Digite algo: ')
resultado = soma_concaterna(valor1, valor2)
print(f'O resultado da soma ou concaternação de {valor1} + {valor2} é igual a {resultado}\n')





assert soma(n1, n2) == n1 + n2
assert multiplica(mult1, mult2, mult3) == mult1 * mult2 * mult3
assert soma_concaterna(valor1, valor2) == valor1 + valor2
