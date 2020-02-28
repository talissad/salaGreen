# Um espaço binário dentro de um número inteiro positivo N é qualquer sequência máxima 
# de zeros consecutivos que é cercada por um em ambas as extremidades na representação binária de N.
# Por exemplo, o número 9 tem representação binária 1001 e contém um espaço binário de comprimento 2. 
# O número 529 tem representação binária 1000010001 e contém duas lacunas binárias: uma de comprimento 4 e outra de comprimento 3. 
# O número 20 tem representação binária 10100 e contém um espaço binário de comprimento 1. O número 15 tem representação binária 1111 
# e não possui espaços binários. O número 32 tem representação binária 100000 e não possui lacunas binárias.

# Escreva uma função:
# solução def (N)

# que, dado um número inteiro positivo N, retorna o comprimento de seu maior intervalo binário. A função deve retornar
#  0 se N não contiver um espaço binário.
# Por exemplo, dado N = 1041, a função deve retornar 5, porque N tem representação binária 10000010001 e, portanto, 
# seu maior intervalo binário é de comprimento 5. Dado N = 32, a função deve retornar 0, porque N tem representação binária 
# '100000' e, portanto, sem lacunas binárias.
# Escreva um algoritmo eficiente para as seguintes suposições:

# N é um número inteiro dentro do intervalo [ 1 .. 2.147.483.647 ].

def solution(N):
    binario = int(N)
    if binario >=1 and binario <= 2147483647:
        n = bin(N)[2:]
        anterior = ''
        lacuna = 0
        for numero in n:
            if numero != anterior and anterior == '0':
                lacuna += 1
            anterior = numero

        contador = n.split('1')
        lista = [contador]
        lista.pop
        if lacuna >= 1:
            gap = len(max(contador))
            return gap
        else:
            return
    else: 
        return

solution(15)

