def fib(n, calls):
    calls.append(n)
    
    if n == 0: return 0
    if n == 1: return 1
    
    return fib(n - 1, calls) + fib(n - 2, calls)

n = int(input(''))

res = []

for i in range(n):
    value = int(input(''))
    
    calls = []
    fib_n = fib(value, calls)
    
    res.append([value, len(calls) - 1, fib_n])

print('')

for data in res:
    print(f'fib({data[0]}) = {data[1]} calls = {data[2]}')