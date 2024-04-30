"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamentp [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[0:5]) # o python sempre vai ignorar o "f", bom adicionar mais 1 casa

print(len(variavel[0:5])) # len checa o tamanho de um str

print(variavel[0:9:2]) # 2 é o passo, vai pulando de casa em casa de acordo com a quantidade colocada

print(variavel[::-1]) # vai inverter, no caso de i e f, precisam ser negativos :)