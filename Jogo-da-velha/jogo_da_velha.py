from random import randint


def main():
    print(' JOGO DA VELHA '.center(50, '='))
    jogo()


def jogo():
    pos: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    gera_tabuleiro(pos)

    if quem_inicia():
        print(f'\nJogador 1 começa!\n')
        jogador: int = 1
    else:
        print(f'\nJogador 2 começa!\n')
        jogador: int = 2

    while not alguem_ganhou(pos):
        # gera_tabuleiro(pos)
        jogada: int = int(input(f'Escolha uma posição do tabuleiro para jogar, Jogador {jogador}: '))
        print('')
        if jogador == 1:
            if jogada in pos:
                pos[jogada - 1] = 'X'
                jogador = 2
                gera_tabuleiro(pos)
            else:
                print(f'Essa jogada já foi escolhida.')
        elif jogador == 2:
            if jogada in pos:
                pos[jogada - 1] = 'O'
                jogador = 1
                gera_tabuleiro(pos)
            else:
                print('Essa jogada já foi escolhida.')

    if alguem_ganhou(pos):
        if jogador == 1:
            print(f'Jogador 2 ganhou a partida!')
        elif jogador == 2:
            print(f'Jogador 1 ganhou a partida!')

    else:
        print('Jogo deu Velha!')

    continuar = int(input('Desejam jogar outra partida? [1 - sim, 2 - não]: '))
    if continuar == 1:
        jogo()
    else:
        print('Até a Próxima!')


def gera_tabuleiro(pos: list) -> None:
    print(f'  {pos[0]}  |  {pos[1]}  |  {pos[2]}  \n'
          f'-----------------\n'
          f'  {pos[3]}  |  {pos[4]}  |  {pos[5]}  \n'
          f'-----------------\n'
          f'  {pos[6]}  |  {pos[7]}  |  {pos[8]}  ')


def quem_inicia() -> int:
    return randint(0, 1)


def alguem_ganhou(pos: list) -> bool:
    if pos[0] == 'X' and pos[1] == 'X' and pos[2] == 'X' or pos[0] == 'O' and pos[1] == 'O' and pos[2] == 'O':
        return True
    elif pos[3] == 'X' and pos[4] == 'X' and pos[5] == 'X' or pos[3] == 'O' and pos[4] == 'O' and pos[5] == 'O':
        return True
    elif pos[6] == 'X' and pos[7] == 'X' and pos[8] == 'X' or pos[6] == 'O' and pos[7] == 'O' and pos[8] == 'O':
        return True
    elif pos[0] == 'X' and pos[3] == 'X' and pos[6] == 'X' or pos[0] == 'O' and pos[3] == 'O' and pos[6] == 'O':
        return True
    elif pos[1] == 'X' and pos[4] == 'X' and pos[7] == 'X' or pos[1] == 'O' and pos[4] == 'O' and pos[7] == 'O':
        return True
    elif pos[2] == 'X' and pos[5] == 'X' and pos[8] == 'X' or pos[2] == 'O' and pos[5] == 'O' and pos[8] == 'O':
        return True
    elif pos[0] == 'X' and pos[4] == 'X' and pos[8] == 'X' or pos[0] == 'O' and pos[4] == 'O' and pos[8] == 'O':
        return True
    elif pos[2] == 'X' and pos[4] == 'X' and pos[6] == 'X' or pos[2] == 'O' and pos[4] == 'O' and pos[6] == 'O':
        return True
    else:
        return False


if __name__ == '__main__':
    main()
