a = 'A'
b = 'B'
c = 1.1

# Segundo tipo de formatação .format()

string = 'a={}, b={}, c={nome3:.2f}' # => índice -> {0}, {1}, {2}...
formato = string.format(a, b, nome3=c) # (..., ...) <- args

print(formato)