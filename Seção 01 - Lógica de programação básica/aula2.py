# \r\n -> CRLF
# \n -> LF - Ambos são quebras de linha

print(12, 34, 1011, sep="-", end='\r\n')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

# sep='' significa, "com o que vai separar?", o valor dentro de '' é o separador.

# end='' significa, "colocar no final", o valro dentro de '' é o que vai ser colocado.