from random import randint


class Calcular:

    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 - Soma, 2 - Subtração, 3 - Multiplicação
        self.__resultado: int = self._gera_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 1000000)

    @property
    def simbolo_operacao(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        else:
            return f'Essa Operação é inválida!'

    @property
    def _gera_resultado(self: object) -> int:
        if self.operacao == 1:  # SOMAR
            return self.valor1 + self.valor2
        elif self.operacao == 2:  # SUBTRAÇÃO
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    def checar_resultado(self: object, resposta: int) -> bool:
        checar: bool = False

        if resposta == self.resultado:
            print(f'A resposta está correta!')
            checar: bool = True
        else:
            print(f'A resposta está errada!')

        print(f'{self.valor1} {self.simbolo_operacao} {self.valor2} = {self.resultado}')
        return checar

    def mostra_operacao(self: object) -> None:
        print(f'{self.valor1} {self.simbolo_operacao} {self.valor2} = ?')
