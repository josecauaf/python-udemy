# Conversão de tipos, coerção, type convertion, typecasting, coercion é o ato de converter um tipo em outro tipos imutáveis e primitivos: str, int, float, bool.
print(int('1'), type(int('1'))) # Conversão para int
print(int('1') + 1)

print(str(1) + '1') # Conversão para str

print(float('1.2') + 1) # Conversão para float

print('Falso => ', bool(''), ' Veradeiro => ', bool(' '))
# bool() sem valor => falso, com valor => verdadeiro