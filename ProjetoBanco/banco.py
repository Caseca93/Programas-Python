from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta
from utils.helper import formata_texto

contas: List[Conta] = []


def main() -> None:
	menu()


def menu() -> None:
	print(formata_texto('='))
	print(formata_texto('*** Caixa Automático ***'))
	print(formata_texto('='))

	print(' Selecione uma das operações abaixo '.upper().center(61, '='))
	print('1 - Criar Conta')
	print('2 - Efetuar Saque')
	print('3 - Efetuar Depósito')
	print('4 - Efetuar Transferência')
	print('5 - Listar Contas')
	print('6 - Sair do Sistema')

	try:
		opcao: int = int(input())

		if opcao == 1:
			criar_conta()
		elif opcao == 2:
			efetuar_saque()
		elif opcao == 3:
			efetuar_deposito()
		elif opcao == 4:
			efetuar_transferencia()
		elif opcao == 5:
			listar_contas()
		elif opcao == 6:
			print('Saída efetuada com sucesso!')
			exit(0)
		else:
			print('Opção inválida, por favor tente novamente.')
			sleep(2)
			menu()
	except ValueError:
		print('Por favor seleciona uma opção!')
		sleep(2)
		menu()


def criar_conta() -> None:
	print(formata_texto('Informe os dados do cliente:'))

	nome: str = input('Nome do Cliente: ')
	email: str = input('Email do Cliente: ')
	cpf: str = input('CPF do Cliente: ')
	data_nascimento: str = input('Data de nascimento do cliente: ')

	cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

	conta: Conta = Conta(cliente)

	contas.append(conta)

	print(formata_texto(' Conta criado com sucesso! '))
	print(formata_texto('='))
	print(conta)
	sleep(2)
	menu()


def efetuar_saque() -> None:
	if len(contas) > 0:
		numero: int = int(input('Informe o número da sua conta: '))

		conta: Conta = busca_conta_por_numero(numero)

		if conta:
			valor: float = float(input('Insira o valor a ser sacado: '))

			conta.sacar(valor)
		else:
			print('O número da conta não foi encontrado. ')

	else:
		print('Não tem nenhuma conta cadastrada.')
	sleep(2)
	menu()


def efetuar_deposito() -> None:
	if len(contas) > 0:
		numero: int = int(input('Informe o número da sua conta: '))

		conta: Conta = busca_conta_por_numero(numero)

		if conta:
			valor: float = float(input('Insira o valor a se depositada: '))

			conta.depositar(valor)
		else:
			print('Essa conta não foi encontrada.')

	else:
		print('Não tem nenhuma conta cadastrada.')
	sleep(2)
	menu()


def efetuar_transferencia() -> None:
	if len(contas) > 0:
		numero_origem: int = int(input('Informe o número da sua conta: '))

		conta_origem: Conta = busca_conta_por_numero(numero_origem)

		if conta_origem:
			numero_destino: int = int(input('Informe a conta para a transferência: '))

			conta_destino: Conta =  busca_conta_por_numero(numero_destino)

			if conta_destino:
				valor: float = float(input('Informe o valor para a transferência: '))

				conta_origem.transferencia(conta_destino, valor)
			else:
				print('A conta de destino não foi encontrada.')
		else:
			print('A conta de origem não foi encontrada.')

	else:
		print('Não tem nenhuma conta cadastrada.')
	sleep(2)
	menu()


def listar_contas() -> None:
	if len(contas) > 0:
		print(formata_texto('Listagem das Contas'))

		for c in contas:
			print(c)
			print(formata_texto('='))
			sleep(2)
	else:
		print('Não tem nenhuma conta cadastrada.')
	sleep(2)
	menu()


def busca_conta_por_numero(numero: int) -> Conta:
	c: Conta = None

	for conta in contas:
		if conta.codigo == numero:
			c = conta
	return c


if __name__ == '__main__':
	main()
