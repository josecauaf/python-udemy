# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3       |
# J o s é       |
#-4-3-2-1       v

nome = 'José'
print(nome[2]) # s
print(nome[-2]) # s
print('---------------')
print('a' in nome) # False
print('o' in nome) # True
print('---------------')
print('a' not in nome) # True
print('o' not in nome) # False
print('---------------')

nome_inp = input('Digite seu nome -> ')
encontrar = input('Digite o que deseja encontrar -> ')

if encontrar in nome_inp:
    print(f'{encontrar} está em {nome_inp}')
else:
    print(f'{encontrar} não está em {nome_inp}')
