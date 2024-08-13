"""
Introdução ao desempacotamento + tuples (tuplas)
"""

nomes =['Maria', 'Helena', 'José']

#nome1,nome2, nome3 = nomes
nome1, *resto = nomes # *_
#_, nome2, *_ = nomes
#_, _, nome3, *_ = nomes

print(nome1, resto)