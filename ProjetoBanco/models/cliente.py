from datetime import date
from datetime import datetime
from time import time

from utils.helper import data_para_str, str_para_data, hora_para_str


class Cliente:
    contador: int = 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_para_data(data_nascimento)
        self.__data_cadastro: date = date.today()
        self.__hora_do_cadastro: time = datetime.now().time()
        Cliente.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:
        return data_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self: object) -> str:
        return data_para_str(self.__data_cadastro)

    @property
    def hora_do_cadastro(self: object) -> str:
        return hora_para_str(self.__hora_do_cadastro)

    def __str__(self: object) -> str:
        return f'Código: {self.codigo}\nNome: {self.nome}\nEmail: {self.email}\nCPF: {self.cpf}\n' \
               f'Data de Nascimento: {self.data_nascimento}\nData do Cadastro: {self.data_cadastro}' \
               f'\nHora do Cadastro: {self.hora_do_cadastro}'
