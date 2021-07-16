# Teste Simples

lista: list = [1, 2, 3, 4, 5, 6]
num = 4
tabuleiro = f'{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]}, {lista[5]}'

lista[5] = 'X'
print(lista)

tabuleiro = f'{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]}, {lista[5]}'
print(tabuleiro)
