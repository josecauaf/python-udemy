# texto = 'Python'
#
# i = 0
# tamanho_string = len(texto)
# 
# while i < tamanho_string:
#     print(texto[1])
# 
#     i +=

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')