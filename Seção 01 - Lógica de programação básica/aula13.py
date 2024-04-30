nome = 'José Cauã'
idade = 20
altura = 1.86
peso = 87
imc = peso / altura ** 2

# Primeiro tipo de formatação (f-strings)

linha_1 = f'{nome} tem {altura:.2f} de altura, '
linha_2 = f'pesa {peso} quilos e seu imc é: '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)