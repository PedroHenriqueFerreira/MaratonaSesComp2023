n = int(input(''))

res = []

for i in range(n):
    a, b, c = [int(v) for v in input('').split(' ')]
    
    delta = (b ** 2) - 4 * a * c
    
    x1 = (- b + (delta ** 0.5)) / (2 * a)
    x2 = (- b - (delta ** 0.5)) / (2 * a)
    
    x = (x1 + x2) / 2
    
    res.append(a * (x ** 2) + b * x + c)

print('')
    
for value in res:
    print(value)