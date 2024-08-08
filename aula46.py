"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Creat  Read  Update  Delete
Criar, ler, alterar, apagar = lista[1] (CRUD)
"""
#........0....1...2...3
lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2])
lista.append(50) # vai adicionar o valor 50 no final da lista
lista.pop() # vai remover o último valor da lista