n = int(input(''))

cedulas = [100, 50, 20, 10, 5, 2, 1]

print('')

for cedula in cedulas:
    qtd = n // cedula
    n -= qtd * cedula
    
    print(f'{qtd} nota(s) de R$ {cedula},00')