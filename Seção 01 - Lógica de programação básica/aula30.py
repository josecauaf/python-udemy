"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar, caso o usuário não digite um número inteiro, informe que não é um número inteiro
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exbia a saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

# Programa 01
print('=-= Programa 01 =-=')

numero_inteiro_do_usuario = input('Olá, usuário! Por favor, digite um número inteiro -> ')

numero_e_inteiro = numero_inteiro_do_usuario.isdigit()
numero_inteiro = None
impar_ou_par = None

if numero_e_inteiro:
    numero_inteiro = int(numero_inteiro_do_usuario)
    impar_ou_par = numero_inteiro % 2
else:
    print('Você precisa digitar um número inteiro!')
    quit()

if impar_ou_par == 0:
    print(f'Número digitado = {numero_inteiro}, o mesmo é par.')
else:
    print(f'Número digitado = {numero_inteiro}, o mesmo é impar.')
#--------------------------------------------------------------

# Programa 02
print('\n=-= Programa 02 =-=')

hora_do_usuario = input('Olá novamente, usuário, por favor, me informe o seu horário atual (ex. 2, 5, 13, 21...) -> ')

verificacao_horario = hora_do_usuario.isdigit()
horario = None

if verificacao_horario:
    horario = int(hora_do_usuario)
else:
    print('Você precisa digitar um horário válido! (inteiro, ex 5, 10, 17, 22...)')

horario_manha = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11    
horario_tarde = 12, 13, 14, 15, 16, 17
horario_noite = 18, 19, 20, 21, 22, 23

if horario in horario_manha:
    print('Bom dia, usuário!')
elif horario in horario_tarde:
    print('Boa tarde, usuário!')
elif horario in horario_noite:
    print('Boa noite, usuário!')
else:
    print('Ops! Valor inesperado. :|')
    quit()
#--------------------------------------------------------------

# Programa 03
print('\n=-= Programa 03 =-=')

nome_do_usuario = input('Olá mais uma vez, usuário! Você poderia me informar seu nome agora? -> ')

tamanho_nome_do_usuario = len(nome_do_usuario)

if tamanho_nome_do_usuario <= 3:
    print('Seu nome é meio curto...')
elif tamanho_nome_do_usuario <= 5:
    print('Érr, seu nome tem um tamanho normal.')
else:
    print('OK! Seu nome é grande demais!')

print('\n\nFim da apresentação! :)\n\n')