n1, n2, n3 = [float(n) for n in input('').split(' ')]

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print(f'Perimetro = {sum([n1, n2, n3]):.1f}')
else:
    print(f'Area = {(((n1 + n2) * n3) / 2):.1f}')