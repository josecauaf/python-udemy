print('Bem-vindo(a) ao script de reconhecimento de valor maior, igual ou             menor que outro valor!\n')            
        
valor01 = input('Digite o primeiro valor -> ')            
valor01_bool = valor01.isnumeric()            
        
if valor01_bool:            
    print(f'\nValor 01 inserido = {valor01}\n')            
else:            
    print('\nOpa! Digite apenas números. :)\n')            
    quit()            
        
valor02 = input('Agora digite o segundo valor -> ')            
valor02_bool = valor02.isnumeric()            
        
if valor02_bool:            
    print(f'\nValor 02 inserido = {valor02}')            
else:            
    print('\nOpa! Digite apenas números. :)\n')            
    quit()            
        
valor01 = int(valor01)            
valor02 = int(valor02)                
        
if valor01 > valor02:            
    print(f'\n-=-=- {valor01} é maior que {valor02} -=-=-\n')            
elif valor01 >= valor02:            
    print(f'\n-=-=- {valor01} é igual a {valor02} -=-=-\n')            
else:            
    print(f'\n-=-=- {valor01} é menor que {valor02} -=-=-\n')            