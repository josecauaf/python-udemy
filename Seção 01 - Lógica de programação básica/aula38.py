"""Calculadora com while"""

while True:
    conta = None

    numero_1 = input('Digite um número -> ')
    numero_valido_1 = numero_1.isdigit()
    if numero_valido_1:
        numero_1 = int(numero_1)
    else:
        print('Digite um valor válido!')
        continue

    numero_2 = input('Digite outro número -> ')
    numero_valido_2 = numero_2.isdigit()
    if numero_valido_2:
        numero_2 = int(numero_2)
    else:
        print('Digite um valor válido!')
        continue
    
    operador = input('Digite um operador (+, -, /, *) -> ')

    if operador == '+':
        conta = numero_1 + numero_2
        print(f'O resultado da sua adição é: {conta}')
    elif operador == '-':
        conta = numero_1 - numero_2
        print(f'O resultado da sua subtração é: {conta}')
    elif operador == '*':
        conta = numero_1 * numero_2
        print(f'O resultado da sua multiplicação é: {conta}')
    elif operador == '/':
        conta = numero_1 / numero_2
        print(f'O resultado da sua divisão é: {conta}')
    else:
        print('Digite um operador válido!')
        continue

    saida = input('Deseja sair? [s]im ou [n]ão')
    saida = saida.lower()
    saida = saida.startswith('s')
    if saida:
        break



    