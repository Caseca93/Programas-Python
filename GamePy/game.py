from models.calcular import Calcular


def main():
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe a dificuldade desejada [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)
    print('Informe o resultado da operação abaixo: ')
    calc.mostra_operacao()
    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Você deseja continuar jogando? [1 - sim, 0 - não] '))
    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou o jogo com {pontos} ponto(s).')
        print(f'Obrigado por jogar, até a próxima.')


if __name__ == '__main__':
    main()
