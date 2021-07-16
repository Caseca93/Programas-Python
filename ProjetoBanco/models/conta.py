from models.cliente import Cliente
from utils.helper import formata_moeda_real


class Conta:
    contador: int = 9001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__codigo: int = Conta.contador
        self.__cliente: cliente = cliente
        self.__saldo: float = 0
        self.__limite: float = 100
        self.__saldo_total = self.calcula_saldo_total
        Conta.contador += 1

    def __str__(self: object) -> str:
        return f'Número da conta: {self.codigo}\nNome do Cliente: {self.cliente.nome}\n' \
               f'Saldo Total: {formata_moeda_real(self.saldo_total)}'

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self.calcula_saldo_total
            print('Depósito efetuado com sucesso.')
        else:
            print('Erro ao efetuar o depósito, tente novamente.')

    def sacar(self: object, valor: float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
            else:
                sobra: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + sobra
                self.saldo_total = self.calcula_saldo_total
            print('Saque efetuado com sucesso.')
        else:
            print('Saldo insuficiente para realização de saque.')

    def transferencia(self: object, conta_destino: object, valor: float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
                conta_destino.saldo = conta_destino.saldo + valor
                conta_destino.saldo_total = conta_destino.calcula_saldo_total
            else:
                sobra: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + sobra
                self.saldo_total = self.calcula_saldo_total
                conta_destino.saldo = conta_destino.saldo + valor
                conta_destino.saldo_total = conta_destino.calcula_saldo_total
            print('Transferência realizada com sucesso.')
        else:
            print('Erro ao efetuar transferência.')
