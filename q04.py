n = int(input(''))

bills = [100, 50, 20, 10, 5, 2, 1]

print('')

for bill in bills:
    qtd = n // bill
    n -= qtd * bill
    
    print(f'{qtd} nota(s) de R$ {bill},00')