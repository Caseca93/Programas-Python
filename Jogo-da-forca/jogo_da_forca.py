# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
O   |
    |
    |
    |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe

class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word:
            return True
        return False

    # Método para verificar se o jogo terminou
    def hangman_over(self, palavra, lista):
        if palavra == self.word or self.print_game_status(lista) == board[6]:
            return True
        return False

    # Método para verificar se o jogador venceu
    def hangman_won(self, palavra):
        if palavra == self.word:
            return True
        return False

    # Método para não mostrar a palavra no board.
    def hide_word(self):
        lista = []
        for i in range(len(self.word)):
            lista.append('_')
        lista = ''.join(lista)

        return lista

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self, lista):
        if len(lista) == 1:
            return board[1]

        elif len(lista) == 2:
            return board[2]

        elif len(lista) == 3:
            return board[3]

        elif len(lista) == 4:
            return board[4]

        elif len(lista) == 5:
            return board[5]

        elif len(lista) == 6:
            return board[6]

        return board[0]


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Varivéis criados para o Programa
    letras_erradas = []

    letras_corretas = []

    palavra = game.word

    lista_palavras = []

    for i in range(len(palavra)):
        lista_palavras.append('_')

    x = 0
    z = 0
    lista_letras_digitadas = []

    lista_palavras2 = ''.join(lista_palavras)

    letras_corretas2 = '  '.join(letras_corretas)

    letras_erradas2 = ''.join(letras_erradas)

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    while not game.hangman_over(lista_palavras2, letras_erradas2):
        print(game.print_game_status(letras_erradas2))
        n = True
        if x == 0:
            print(f'\nPalavra: {game.hide_word()}')
        else:
            print(f'\nPalavra: {lista_palavras2}')

        print(f'\nLetras erradas:\n{letras_erradas2}')
        print(f'\nLetras Certas:\n{letras_corretas2}')

        if '_' in lista_palavras2:
            while n:
                letra = input('\nDigite uma letra: ')
                if z == 0:
                    lista_letras_digitadas.append(letra)
                    n = False
                    print(lista_letras_digitadas)
                elif z == 1:
                    if letra in lista_letras_digitadas:
                        print(game.print_game_status(letras_erradas2))
                        if x == 0:
                            print(f'\nPalavra: {game.hide_word()}')
                        else:
                            print(f'\nPalavra: {lista_palavras2}')
                        print(f'\nLetras erradas:\n{letras_erradas2}')
                        print(f'\nLetras Certas:\n{letras_corretas2}')
                        # letra = input('\nDigite uma letra: ')
                    else:
                        lista_letras_digitadas.append(letra)
                        n = False
            z = 1

            if game.guess(letra):
                for le in range(len(palavra)):
                    if palavra[le] == letra:
                        lista_palavras[le] = letra
                        lista_palavras2 = ''.join(lista_palavras)
                x = 1
                letras_corretas.append(letra)
                letras_corretas2 = '  '.join(letras_corretas)

            else:
                letras_erradas.append(letra)
                letras_erradas2 = ''.join(letras_erradas)

        else:
            lista_palavras = ''.join(lista_palavras)

    print(game.print_game_status(letras_erradas))
    print(f'\nPalavra: {lista_palavras2}')
    print(f'\nLetras erradas:\n{letras_erradas2}')
    print(f'\nLetras Certas:\n{letras_corretas2}')

    # De acordo com o status, imprime mensagem na tela para o usuário.
    if game.hangman_won(lista_palavras2):
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()