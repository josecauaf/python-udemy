# Crie um gerador de CPF válidos!

import random

cpf = 0
cpf_base = ''
resultado_digito_1 = 0
resultado_digito_2 = 0

for i in range(9):
    cpf_base += str(random.randint(0, 9))

cpf_indices = list(cpf_base)

contador_regressivo = 10

for digito in cpf_indices:
    resultado_digito_1 += int(digito) * contador_regressivo
    contador_regressivo -= 1

digito_1 = (resultado_digito_1 * 10) % 11 
digito_1 = digito_1 if digito_1 <= 9 else 0 

###

cpf_indices.append(str(digito_1))

contador_regressivo = 11

for digito in cpf_indices:
    resultado_digito_2 += int(digito) * contador_regressivo
    contador_regressivo -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_indices.append(str(digito_2))

for digito in cpf_indices:
    print(digito, end='', sep='')