from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print(' Bem-Vindo(a) '.center(61, '='))
    print(' Caseca Shop '.center(61, '='))

    print('Escolha uma das opções abaixo:')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Vizualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')
    try:
        opcao: int = int(input())

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produto()
        elif opcao == 3:
            comprar_produto()
        elif opcao == 4:
            vizualizar_carrinho()
        elif opcao == 5:
            fechar_pedido()
        elif opcao == 6:
            print('Obrigado por comprar conosco, volte sempre!')
            sleep(2)
            exit(0)
        else:
            print('Ops, opcão inválida! Por favor, tente novamente.')
            sleep(2)
            menu()
    except ValueError:
        print('Ops! Parece que você esqueceu de digitar uma opção né amigo! Tente novamente.')
        sleep(2)
        menu()


def cadastrar_produto() -> None:
    print(' Cadastrar Produto '.center(61, '='))

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso.')
    sleep(2)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print(' Listagem dos Produtos '.center(61, '='))
        for produto in produtos:
            print(produto)
            print('----------'.center(61, '-'))
            sleep(1)
    else:
        print('Ainda não tem nenhum produto cadastrado.')
    sleep(1)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('Produtos Disponiveis'.center(61, '='))
        for produto in produtos:
            print(produto)
            print('------------------------------------'.center(61, '-'))
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod: dict = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado. ')

    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()


def vizualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print(' Produtos no Carrinho '.center(61, '='))

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------'.center(61, '-'))
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print(' Produtos no Carrinho '.center(61, '='))

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_individual = dados[0].preco * dados[1]
                print(f'Valor : {formata_float_str_moeda(valor_individual)}')
                valor_total += dados[0].preco * dados[1]
                print('--------------'.center(61, '-'))
                sleep(1)
        print(f'O total das suas compras deu {formata_float_str_moeda(valor_total)} reais.')
        print('Obrigado por comprar conosco e volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existe produtos no seu carrinho!')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if codigo == produto.codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
