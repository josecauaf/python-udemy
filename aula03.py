"""
CÁLCULO DO PRIMEIRO DÍGITO DO CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.: 746.846.890-70 (746824890)
   10 9  8  7  6  5  4  3  2
   7  4  6  8  2  4  8  9  0
   70 35 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 - 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
condicao = True

while condicao:

    cpf_v1 = input("Vamos descobrir o primeiro dígito verificador, digite os primeiro 9 digitos do CPF -> ")
    cpf_v2 = cpf_v1.replace('.', '')
    cpf_v3 = cpf_v2.replace('-', '')

    cpf_len = len(cpf_v3)

    try:
        cpf_int = int(cpf_v3)
    except:
        print('Digite apenas o seu CPF! xxx.xxx.xxx ou xxxxxxxxx')
    
    if (cpf_len < 9):
        print('Digite os 9 dígitos do seu CPF!')
        continue
    elif (cpf_len > 9):
        print('Você digitou números demais, digite apenas os 9 dígitos do seu CPF!')
        continue

    cpf_tuple = tuple(str(cpf_int))

    cpf_1 = int(cpf_tuple[0])
    cpf_2 = int(cpf_tuple[1])
    cpf_3 = int(cpf_tuple[2])
    cpf_4 = int(cpf_tuple[3])
    cpf_5 = int(cpf_tuple[4])
    cpf_6 = int(cpf_tuple[5])
    cpf_7 = int(cpf_tuple[6])
    cpf_8 = int(cpf_tuple[7])
    cpf_9 = int(cpf_tuple[8])

    multiplicacao_1 = cpf_1 * 10
    multiplicacao_2 = cpf_2 * 9
    multiplicacao_3 = cpf_3 * 8
    multiplicacao_4 = cpf_4 * 7
    multiplicacao_5 = cpf_5 * 6
    multiplicacao_6 = cpf_6 * 5
    multiplicacao_7 = cpf_7 * 4
    multiplicacao_8 = cpf_8 * 3
    multiplicacao_9 = cpf_9 * 2

    soma_total = multiplicacao_1 + multiplicacao_2 + multiplicacao_3 + multiplicacao_4 + multiplicacao_5 + multiplicacao_6 + multiplicacao_7 + multiplicacao_8 + multiplicacao_9

    multiplicacao_total = soma_total * 10

    primeiro_digito_verificador = multiplicacao_total % 11

    if (primeiro_digito_verificador > 9):
        primeiro_digito_verificador = 0
    
    print(f'O primeiro dígito verificador é: {primeiro_digito_verificador}')
    break


#CÓDIGO DO LUIZ
"""
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
"""


