"""
Listas em Python
Tipo lista - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - Apaga um indice
    clear - Limpa a lista
    extend - Estende a lista
    + = Concatena listas
Creat, Read, Update, Delete
Criar, Ler, Alterar, Apagar = lista[1] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('José')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear() # limpa a lista
lista.insert(0, 5) # insere em um determinado valor, sendo o primeiro o índice, depois o valor
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5 ,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)