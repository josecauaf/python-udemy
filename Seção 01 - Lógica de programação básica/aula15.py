# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
int_bool_1 = numero_1.isnumeric()
int_1 = ''

if int_bool_1 == True:
    int_1 = int(numero_1)
else:
    print('Digite um valor válido para o número 1!')
    quit()

numero_2 = input('Digite outro número: ')
int_bool_2 = numero_1.isnumeric()
int_2 = ''

if int_bool_1 == True:
    int_2 = int(numero_2)
else:
    print('Digite um valor válido para o número 2!')
    quit()

print(f'A soma dos números é: {int_1 + int_2}')