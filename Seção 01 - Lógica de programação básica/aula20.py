# Operadores lógicos
# and (e) or (ou) not (não)
# and = Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
# São consideradors False
# 0 0.0 '' False (já vistos)
# Também existe o tipo None que é usado para representar um não valor

# CÓDIGO ABAIXO É APENAS PARA EXEMPLO, NÃO UTILIZAR DE FORMA PROFISSIONAL
entrada = input('[E] -> Entrar | [S] -> Sair : ')
senha_digitada = input('Senha -> ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair') 

# Avaliação de curto circuito
print(True and True and True) # -> True
print(True and False and True) # -> False