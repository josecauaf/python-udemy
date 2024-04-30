"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> = Esquerda
< - Direita
^ - Centro
= - FOrça o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Cnversion flags - !r !s !a __repr__ __str__ __ask__
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{1000.299542935934:.1f}') # :,.1f, se negativo :-,.1f (ou + positivo), :0=+10,.1f
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel}')