"""
Iterando strings com while
"""
#       012345678
nome = 'José Cauã' # Iterável
#      -897654321

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += letra
    indice += 1

print(novo_nome)