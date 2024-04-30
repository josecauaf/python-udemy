"""
Exercício
Peça o usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não espaços)
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios
"""

print('Seja super bem-vindo(a) ao identificador de sequências multiplas!\n')

nome = input('Para começar, digite seu nome -> ')
nome_null = len(nome)

if nome_null == 0:
    print('Desculpe, mas você não digitou nada :|')
    quit()
else:
    print(f'\nNome escolhido: {nome}')

idade = input('\nAgora digite sua idade -> ')
idade_is_num = idade.isnumeric()

if idade_is_num:
    print(f'\n1. Seu nome é {nome}')
    print(f'2. Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'3. Seu nome contém espaço(s)')
    else:
        print(f'3. Seu nome não contém espaço')
    print(f'4. Seu nome tem {len(nome)} letras (contando com espaços)')
    print(f'5. A primeira letra do seu nome é: {nome[0]}')
    print(f'6. A última letra do seu nome é {nome[-1]}')
else:
    print('\nDigite apenas números na idade :|')