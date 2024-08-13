"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

lista = []
variavel_raiz = True

while variavel_raiz:
    opcao1 = input('\n-=- Lista de compras automático -=-\n> Selecione uma opção: \n[I]nserir | [A]pagar | [L]istar | [S]air -> ')

    if (opcao1 == 'I') or (opcao1 == 'i'):
        valor1 = input('\nO que deseja inserir na lista de compras? -> ')
        lista.append(valor1)
        print(f'\nO item "{valor1}" foi inserido com sucesso!')
        continue
    elif (opcao1 == 'a') or (opcao1 == 'A'):
        if lista == []:
            print('\nNão há nada para apagar.')
            continue
        print('\n|ITENS NA LISTA|\n')
        for indice, item in enumerate(lista):
            print(f'[{indice}] > {item}')
        valor2 = input('\nDigite o índice do item que deseja apagar -> ')
        if valor2.isnumeric():
            ...
        else:
            print('\nDigite um índice em número!')
            continue
        valor2 = int(valor2)
        try:
            pega_erro = lista[valor2]
            print(f'\nO item {valor2} foi apagado com sucesso!'), lista.pop(valor2)
        except:
            print('\nNão foi possível apagar este item, talvez não exista?')
            continue
    elif (opcao1 == 'l') or (opcao1 == 'L'):
        if lista == []:
            print('\nNão há nada para listar!')
            continue
        print('\n|LISTA ABAIXO|\n')
        for indice, item in enumerate(lista):
            print(f'> [{indice}] {item}')
            continue
    elif (opcao1 == 's') or (opcao1 == 'S'):
        variavel_raiz = False
        print('\nAté mais! :)\n')
    else:
        print("\nDigite uma opção válida!")
        continue

