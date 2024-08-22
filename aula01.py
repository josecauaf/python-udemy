# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'e', 'legal'

# a, b, c, *_ = lista
# print(a, c)

print(*lista)
print(*string)
print(*tupla)

for nome in lista:
    print(nome, end=' ', sep='')