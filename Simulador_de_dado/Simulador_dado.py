import random

class Simulador:

    def __init__(self) -> None:
        self.__valor_minimo: int = 1
        self.__valor_maximo: int = 6


    def jogar(self) -> int:
        try:
            resposta = input('Você gostaria de jogar o dado, sim ou não? ')
            if resposta == 'sim' or resposta == 's':
                self.GerarValordoDado()
            elif resposta == 'nao' or resposta == 'n':
                print('Obrigado por jogar.')
        except:
            print('O valor informado é inválido.')

    def GerarValordoDado(self) -> int:
        print(random.randint(self.__valor_minimo, self.__valor_maximo))


dado = Simulador()
dado.jogar()
