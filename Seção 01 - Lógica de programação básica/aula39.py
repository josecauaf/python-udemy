string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    #break (código dentro do while para baixo não vai ser executado)

    print(letra)
    i += 1
else:
    print('O else foi executado.')
print('Fora do while.')