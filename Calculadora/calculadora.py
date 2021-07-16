# Calculadora Python!

# Aparece essa frase centralizada na tela com os * no começo e no final da frase
print(' Calculadora Python '.center(50, '*'))

# Aparece essa frase na tela.
print('\nSeleciona o número da opção desejada:')

# Aparece essa frase na tela
print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')

# Uma varável onde vai a opção que o usuario escolheu.
opcao = int(input('\nDigite sua opção (1/2/3/4): '))

# Numeros de entrada que o usuario vai dar.
try:
    num1 = int(input('\nDigite um número: '))
    num2 = int(input('\nDigite outro número: '))

    # confere se a variavel opcao é igual a 1 para ser executada.
    if opcao == 1:
        print(f'\nA soma de {num1} + {num2} = {num1 + num2}. ')

    # caso a primeiro if não for verdade executa esse
    elif opcao == 2:
        print(f'\nA subtração de {num1} - {num2} = {num1 - num2}.')

    # caso os dois não forem verdade, executa esse.
    elif opcao == 3:
        print(f'\nA multiplicação de {num1} * {num2} = {num1 * num2}.')

    # caso os tres não forem verdade, executa esse.
    elif opcao == 4:
        print(f'\nA divisão de {num1} / {num2} = {num1 / num2}.')
    # Se nenhum for verdade, executa esse.
    else:
        print('\nOpção Inválida!')
except ZeroDivisionError:
    print('Não é possível executar uma divisão por zero.')